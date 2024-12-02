"""Fixtures for Twinkly integration tests."""
import pytest
from unittest.mock import MagicMock, patch
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

@pytest.fixture(name="mock_twinkly")
def mock_twinkly_fixture():
    """Create a mock Twinkly device using ttls interface."""
    device = MagicMock()
    # These match the ttls library interface
    device.mac = "AA:BB:CC:DD:EE:FF"
    device.device_name = "Test Twinkly"
    device.is_on = False
    device.brightness = 100
    device.mode = "off"
    
    # Mock the ttls methods
    device.turn_on = MagicMock()
    device.turn_off = MagicMock()
    device.set_brightness = MagicMock()
    
    return device

# @pytest.fixture
# def hass(event_loop) -> HomeAssistant:
#     """Return a Home Assistant instance for testing."""
#     hass = HomeAssistant()
#     # Additional setup...
#     return hass

@pytest.fixture(name="config_entry")
def config_entry_fixture() -> ConfigType:
    """Create a mock config entry."""
    return {
        "domain": "twinkly",  # Make sure to specify your actual domain
        "data": {
            CONF_HOST: "192.168.1.123",
        },
    }

@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Automatically enable custom integrations for all tests."""
    yield