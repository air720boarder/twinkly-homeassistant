"""Test the Twinkly Custom integration."""
import pytest
from unittest.mock import patch, AsyncMock
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_HOST
from pytest_homeassistant_custom_component.common import MockConfigEntry
from homeassistant.helpers.entity_registry import EntityRegistry
from homeassistant.helpers import entity_registry as er

from custom_components.twinkly_custom.const import DOMAIN

@pytest.mark.asyncio
async def test_setup(hass: HomeAssistant):
    """Test the setup."""
    mock_device = AsyncMock()
    mock_device.device_name = "Test Twinkly"
    mock_device.is_on = AsyncMock(return_value=False)
    mock_device.get_brightness = AsyncMock(return_value=100)
    mock_device.mac = "AA:BB:CC:DD:EE:FF"

    with patch(
        "custom_components.twinkly_custom.light.Twinkly",
        return_value=mock_device,
    ):
        entry = MockConfigEntry(
            domain=DOMAIN,
            data={CONF_HOST: "192.168.1.123"},
        )
        entry.add_to_hass(hass)

        # Test the setup
        assert await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()

        # Verify the entity is added
        state = hass.states.get("light.test_twinkly")
        assert state is not None

        # Verify the domain is set up
        assert DOMAIN in hass.config_entries.async_domains()
        assert len(hass.states.async_all()) == 1

@pytest.mark.asyncio
async def test_unload_entry(hass: HomeAssistant):
    """Test unloading the entry."""
    mock_device = AsyncMock()
    mock_device.device_name = "Test Twinkly"
    mock_device.is_on = AsyncMock(return_value=False)
    mock_device.get_brightness = AsyncMock(return_value=100)
    mock_device.mac = "AA:BB:CC:DD:EE:FF"

    with patch(
        "custom_components.twinkly_custom.light.Twinkly",
        return_value=mock_device,
    ):
        entry = MockConfigEntry(
            domain=DOMAIN,
            data={CONF_HOST: "192.168.1.123"},
        )
        entry.add_to_hass(hass)

        # Setup the entry
        assert await hass.config_entries.async_setup(entry.entry_id)
        await hass.async_block_till_done()

        # Verify it's loaded
        assert len(hass.states.async_all()) == 1

        # Unload the entry
        assert await hass.config_entries.async_unload(entry.entry_id)
        await hass.async_block_till_done()

        # Verify the entity state is 'unavailable'
        state = hass.states.get("light.test_twinkly")
        assert state is not None
        assert state.state == "unavailable"