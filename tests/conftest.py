"""Fixtures for Twinkly Custom integration tests."""
import pytest
from unittest.mock import MagicMock, patch
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant

@pytest.fixture(autouse=True)
def auto_enable_custom_integrations(enable_custom_integrations):
    """Enable custom integrations in Home Assistant."""
    yield

@pytest.fixture
def mock_setup_entry() -> None:
    """Override async_setup_entry."""
    with patch(
        "custom_components.twinkly_custom.async_setup_entry",
        return_value=True,
    ):
        yield

@pytest.fixture(name="mock_twinkly")
def mock_twinkly_fixture():
    """Create a mock Twinkly device."""
    device = MagicMock()
    device.mac = "AA:BB:CC:DD:EE:FF"
    device.device_name = "Test Twinkly"
    device.is_on = False
    device.brightness = 100
    device.mode = "off"
    
    # Mock the methods
    device.turn_on = MagicMock()
    device.turn_off = MagicMock()
    device.set_brightness = MagicMock()
    
    return device