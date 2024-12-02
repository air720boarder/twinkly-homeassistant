import logging
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.components import zeroconf
import voluptuous as vol

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)


class TwinklyConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Twinkly Gen2."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step initiated by the user."""
        return await self.async_step_manual(user_input)

    async def async_step_manual(self, user_input=None):
        """Handle manual configuration."""
        errors = {}
        if user_input is not None:
            host = user_input["host"]
            from ttls import Twinkly

            twinkly = Twinkly(host)
            try:
                await self.hass.async_add_executor_job(twinkly.update)
                await self.async_set_unique_id(twinkly.mac)
                self._abort_if_unique_id_configured()
                return self.async_create_entry(title=twinkly.device_name, data=user_input)
            except Exception:
                errors["base"] = "cannot_connect"

        data_schema = vol.Schema({vol.Required("host"): str})
        return self.async_show_form(step_id="manual", data_schema=data_schema, errors=errors)

    async def async_step_zeroconf(self, discovery_info):
        """Handle zeroconf discovery."""
        host = discovery_info["host"]
        name = discovery_info["name"]
        if not name.lower().startswith("twinkly"):
            return self.async_abort(reason="not_twinkly_device")

        from ttls import Twinkly

        twinkly = Twinkly(host)
        try:
            await self.hass.async_add_executor_job(twinkly.update)
            await self.async_set_unique_id(twinkly.mac)
            self._abort_if_unique_id_configured()
            self.context.update({"title_placeholders": {"name": twinkly.device_name}})
            return self.async_create_entry(title=twinkly.device_name, data={"host": host})
        except Exception:
            return self.async_abort(reason="cannot_connect")