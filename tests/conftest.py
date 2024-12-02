"""Fixtures for Twinkly integration tests."""
import pytest

from homeassistant.const import CONF_HOST
from custom_components.twinkly.const import DOMAIN

@pytest.fixture(name="config_entry")
def config_entry_fixture(hass):
    """Create a mock config entry."""
    return {
        "domain": DOMAIN,
        "data": {
            CONF_HOST: "192.168.1.123",
        },
    } 