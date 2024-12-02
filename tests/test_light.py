"""Test the Twinkly Custom light platform."""
import pytest
from unittest.mock import patch, AsyncMock
from homeassistant.core import HomeAssistant
from custom_components.twinkly.const import DOMAIN

@patch("custom_components.twinkly.config_flow.Twinkly")
@pytest.mark.asyncio
async def test_light_turn_on(mock_light_twinkly, hass: HomeAssistant):
    """Test turning on a light."""
    # Setup your mocks
    mock_device = AsyncMock()
    mock_device.is_on = False
    mock_device.mode = "off"
    mock_device.brightness = 100
    mock_device.mac = "AA:BB:CC:DD:EE:FF"
    mock_device.device_name = "Test Twinkly Custom"

    mock_light_twinkly.return_value = mock_device

    # Initialize the config flow
    result = await hass.config_entries.flow.async_init(
        DOMAIN,
        context={"source": "user"},
        data={"host": "192.168.1.123"},
    )

    # Assert the flow results
    assert result["type"] == "create_entry"
    assert result["title"] == "Test Twinkly Custom"
    assert result["data"]["host"] == "192.168.1.123"

    # Additional assertions or operations...
    assert mock_light_twinkly.called