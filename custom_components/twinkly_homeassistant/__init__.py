import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from ttls import Twinkly

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["light"]


async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Twinkly Home Assistant component."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Twinkly lights from a config entry."""
    from ttls import Twinkly

    twinkly = Twinkly(entry.data["host"])
    await hass.async_add_executor_job(twinkly.update)

    hass.data[DOMAIN][entry.entry_id] = twinkly

    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a Twinkly config entry."""
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok