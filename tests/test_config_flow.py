"""Test the Twinkly Custom config flow."""
from unittest.mock import patch

import pytest
from homeassistant import config_entries, data_entry_flow
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant

from custom_components.twinkly_custom.const import DOMAIN

@pytest.mark.asyncio
async def test_form(hass: HomeAssistant):
    """Test we get the form and create an entry."""
    result = await hass.config_entries.flow.async_init(
        DOMAIN, context={"source": config_entries.SOURCE_USER}
    )
    assert result["type"] == data_entry_flow.FlowResultType.FORM
    assert result["errors"] == {}

    # Since there's no connection test, we don't need to patch anything
    result2 = await hass.config_entries.flow.async_configure(
        result["flow_id"],
        {
            CONF_HOST: "192.168.1.123",
        },
    )
    await hass.async_block_till_done()

    assert result2["type"] == data_entry_flow.FlowResultType.CREATE_ENTRY
    assert result2["title"] == "Twinkly Custom"
    assert result2["data"] == {
        CONF_HOST: "192.168.1.123",
    } 