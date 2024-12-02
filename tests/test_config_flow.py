import asyncio

from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from unittest.mock import patch

from custom_components.twinkly.const import DOMAIN

async def test_manual_config_flow(hass: HomeAssistant):
    """Test manual configuration flow."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == "form"
    assert result["step_id"] == "manual"

    with patch(
        "custom_components.twinkly_homeassistant.config_flow.Twinkly.update",
        return_value=True,
    ), patch(
        "custom_components.twinkly_homeassistant.config_flow.Twinkly.mac",
        new_callable=property,
        return_value="AA:BB:CC:DD:EE:FF",
    ):
        result2 = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {"host": "192.168.1.100"},
        )

    assert result2["type"] == "create_entry"
    assert result2["title"] == "Twinkly Device"
    assert result2["data"] == {"host": "192.168.1.100"} 