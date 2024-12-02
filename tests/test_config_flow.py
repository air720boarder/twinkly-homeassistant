"""Test the Twinkly config flow."""
import pytest
from unittest.mock import patch, AsyncMock
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from custom_components.twinkly.const import DOMAIN

@pytest.mark.asyncio
async def test_manual_config_flow(hass: HomeAssistant):
    """Test manual configuration flow."""
    with patch("custom_components.twinkly.config_flow.Twinkly") as mock_twinkly:
        mock_device = AsyncMock()
        mock_twinkly.return_value = mock_device
        mock_device.mac = "AA:BB:CC:DD:EE:FF"
        mock_device.device_name = "Test Twinkly"

        result = await hass.config_entries.flow.async_init(
            DOMAIN, context={"source": config_entries.SOURCE_USER}
        )

        assert result["type"] == "form"
        assert result["step_id"] == "user"

        result = await hass.config_entries.flow.async_configure(
            result["flow_id"],
            {"host": "192.168.1.123"},
        )

        assert result["type"] == "create_entry"
        assert result["title"] == "Test Twinkly" 