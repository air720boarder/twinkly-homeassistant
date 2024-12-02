DOMAIN = "twinkly_gen2"
DEFAULT_NAME = "Twinkly Gen2 Light"
SCAN_INTERVAL = 10  # in seconds

# Supported features
SUPPORTED_FEATURES = (
    SUPPORT_BRIGHTNESS
    | SUPPORT_COLOR
    | SUPPORT_EFFECT
)

# Available effects
EFFECT_LIST = ["movie", "effect", "rt", "off"]