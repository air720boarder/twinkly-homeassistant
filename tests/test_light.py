"""Test the Twinkly Custom light platform."""
from unittest.mock import patch, AsyncMock
from homeassistant.core import HomeAssistant
from homeassistant.const import (
    CONF_HOST,
    STATE_ON,
    STATE_OFF,
)
from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
)

import pytest
from pytest_homeassistant_custom_component.common import MockConfigEntry

from custom_components.twinkly_custom.const import DOMAIN

@pytest.mark.asyncio
async def test_light_setup(hass: HomeAssistant):
    """Test setting up the Twinkly Custom light."""
    mock_device = AsyncMock()
    mock_device.device_name = "Test Twinkly"
    mock_device.is_on = AsyncMock(return_value=False)
    mock_device.get_brightness = AsyncMock(return_value=100)
    mock_device.turn_on = AsyncMock()
    mock_device.turn_off = AsyncMock()
    mock_device.set_brightness = AsyncMock()
    mock_device.update = AsyncMock()
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

        # Verify the entity is added
        entity_id = "light.test_twinkly"
        state = hass.states.get(entity_id)
        assert state is not None
        assert state.state == STATE_OFF

        # Test turning on the light
        await hass.services.async_call(
            "light",
            "turn_on",
            {"entity_id": entity_id, ATTR_BRIGHTNESS: 200},
            blocking=True,
        )
        await hass.async_block_till_done()

        mock_device.turn_on.assert_called_once()
        mock_device.set_brightness.assert_called_with(200)

        # Update the mock to return True for is_on
        mock_device.is_on.return_value = True

        # Force an update of the entity
        await hass.helpers.entity_component.async_update_entity(entity_id)
        await hass.async_block_till_done()

        # Verify the state is now 'on'
        state = hass.states.get(entity_id)
        assert state.state == STATE_ON