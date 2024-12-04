"""Constants for the Twinkly Custom integration."""
from homeassistant.const import Platform
from homeassistant.components.light import (
    ATTR_BRIGHTNESS,
    SUPPORT_BRIGHTNESS,
)

DOMAIN = "twinkly_custom"
PLATFORMS = [Platform.LIGHT]

# Configuration
CONF_HOST = "host"
CONF_NAME = "name"

# Defaults
DEFAULT_NAME = "Twinkly"
SCAN_INTERVAL = 10

# Available effects
EFFECT_MOVIE = "movie"
EFFECT_EFFECT = "effect"
EFFECT_RT = "rt"
EFFECT_OFF = "off"
EFFECT_LIST = [EFFECT_MOVIE, EFFECT_EFFECT, EFFECT_RT, EFFECT_OFF]

# Define supported features if necessary
SUPPORTED_FEATURES = SUPPORT_BRIGHTNESS