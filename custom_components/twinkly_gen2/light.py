import logging
import asyncio

from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    ATTR_HS_COLOR,
    ATTR_EFFECT,
    SUPPORT_BRIGHTNESS,
    SUPPORT_COLOR,
    SUPPORT_EFFECT,
    LightEntity,
)
from homeassistant.helpers.entity import DeviceInfo
from homeassistant.util.color import color_hs_to_RGB, color_RGB_to_hs

from .const import DOMAIN, DEFAULT_NAME, SUPPORTED_FEATURES, EFFECT_LIST

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up Twinkly Gen2 light based on a config entry."""
    twinkly = hass.data[DOMAIN][config_entry.entry_id]
    async_add_entities([TwinklyLight(twinkly)], True)


class TwinklyLight(LightEntity):
    """Representation of a Twinkly Gen2 light."""

    def __init__(self, twinkly):
        """Initialize the light."""
        self._twinkly = twinkly
        self._name = twinkly.device_name or DEFAULT_NAME
        self._unique_id = twinkly.mac
        self._is_on = False
        self._brightness = 255
        self._hs_color = None
        self._effect = None
        self._available = True
        self._device_info = DeviceInfo(
            identifiers={(DOMAIN, self._unique_id)},
            name=self._name,
            manufacturer="Twinkly",
            model=twinkly.product_name,
            sw_version=twinkly.fw_version,
        )

    @property
    def name(self):
        """Return the display name of this light."""
        return self._name

    @property
    def unique_id(self):
        """Return a unique ID for this light."""
        return self._unique_id

    @property
    def supported_features(self):
        """Flag supported features."""
        return SUPPORTED_FEATURES

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._is_on

    @property
    def brightness(self):
        """Return the brightness of this light between 0..255."""
        return self._brightness

    @property
    def hs_color(self):
        """Return the hue and saturation color value."""
        return self._hs_color

    @property
    def effect_list(self):
        """Return the list of supported effects."""
        return EFFECT_LIST

    @property
    def effect(self):
        """Return the current effect."""
        return self._effect

    @property
    def device_info(self):
        """Return device info."""
        return self._device_info

    @property
    def available(self):
        """Return if the device is available."""
        return self._available

    async def async_turn_on(self, **kwargs):
        """Instruct the light to turn on."""
        tasks = []

        if ATTR_BRIGHTNESS in kwargs:
            brightness = int(kwargs[ATTR_BRIGHTNESS] / 2.55)  # Convert 0-255 to 0-100
            tasks.append(
                self.hass.async_add_executor_job(self._twinkly.set_brightness, brightness)
            )
            self._brightness = kwargs[ATTR_BRIGHTNESS]

        if ATTR_HS_COLOR in kwargs:
            rgb_color = color_hs_to_RGB(*kwargs[ATTR_HS_COLOR])
            tasks.append(
                self.hass.async_add_executor_job(self._twinkly.set_static_color, rgb_color)
            )
            self._hs_color = kwargs[ATTR_HS_COLOR]

        if ATTR_EFFECT in kwargs:
            effect = kwargs[ATTR_EFFECT]
            if effect in EFFECT_LIST:
                tasks.append(
                    self.hass.async_add_executor_job(self._twinkly.set_mode, effect)
                )
                self._effect = effect
            else:
                _LOGGER.warning("Unsupported effect: %s", effect)

        if not tasks:
            tasks.append(self.hass.async_add_executor_job(self._twinkly.turn_on))
        else:
            # Ensure the light is on after applying settings
            tasks.append(self.hass.async_add_executor_job(self._twinkly.turn_on))

        await asyncio.gather(*tasks)
        self._is_on = True
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        await self.hass.async_add_executor_job(self._twinkly.turn_off)
        self._is_on = False
        self.async_write_ha_state()

    async def async_update(self):
        """Fetch new state data for this light."""
        try:
            await self.hass.async_add_executor_job(self._twinkly.update)
            self._is_on = self._twinkly.is_on
            self._brightness = int(self._twinkly.brightness * 2.55)
            color = self._twinkly.color
            if color:
                self._hs_color = color_RGB_to_hs(*color)
            else:
                self._hs_color = None
            self._effect = self._twinkly.mode
            self._available = True
        except Exception as e:
            _LOGGER.error("Error updating Twinkly light: %s", e)
            self._available = False