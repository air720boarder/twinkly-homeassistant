"""Constants for the Twinkly Custom integration."""
from homeassistant.const import Platform
from homeassistant.components.light import SUPPORT_BRIGHTNESS

DOMAIN = "twinkly_custom"
PLATFORMS = [Platform.LIGHT]

# Configuration constants
CONF_NAME = "name"

# Default values
DEFAULT_NAME = "Twinkly"

# Define supported features if necessary
SUPPORTED_FEATURES = SUPPORT_BRIGHTNESS