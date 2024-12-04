import logging
from homeassistant.components.light import (
    LightEntity,
    ATTR_BRIGHTNESS,
    SUPPORT_BRIGHTNESS,
    COLOR_MODE_BRIGHTNESS,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN

# Import your Twinkly device class
from ttls.client import Twinkly  # Adjust the import path as necessary

_LOGGER = logging.getLogger(__name__)

DEFAULT_NAME = "Twinkly Light"

async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
):
    """Set up Twinkly Custom Light from a config entry."""
    host = entry.data.get("host")
    twinkly = Twinkly(host)  # Create an instance of the Twinkly device
    await twinkly.login()  # Login if necessary
    async_add_entities([TwinklyLight(twinkly)], True)


class TwinklyLight(LightEntity):
    """Representation of a Twinkly Light."""

    _attr_supported_color_modes = {COLOR_MODE_BRIGHTNESS}
    _attr_color_mode = COLOR_MODE_BRIGHTNESS

    def __init__(self, twinkly_device):
        """Initialize the light."""
        self._device = twinkly_device
        self._attr_name = twinkly_device.device_name
        self._attr_unique_id = twinkly_device.mac
        self._is_on = False
        self._brightness = 0

    @property
    def name(self):
        """Return the name of the light."""
        return self._attr_name

    @property
    def is_on(self):
        """Return true if light is on."""
        return self._is_on

    @property
    def brightness(self):
        """Return the brightness of the light."""
        return self._brightness

    async def async_turn_on(self, **kwargs):
        """Instruct the light to turn on."""
        brightness = kwargs.get(ATTR_BRIGHTNESS, 255)
        await self._device.set_brightness(brightness)
        await self._device.turn_on()
        self._is_on = True
        self._brightness = brightness
        self.async_write_ha_state()

    async def async_turn_off(self, **kwargs):
        """Instruct the light to turn off."""
        await self._device.turn_off()
        self._is_on = False
        self.async_write_ha_state()

    async def async_update(self):
        """Fetch new state data for this light."""
        await self._device.update()
        self._is_on = await self._device.is_on()
        self._brightness = await self._device.get_brightness()

    async def async_will_remove_from_hass(self):
        """Handle entity removal."""
        await super().async_will_remove_from_hass()
        # Perform any additional cleanup here