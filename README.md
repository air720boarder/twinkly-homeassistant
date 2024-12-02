![Twinkly logo](https://mma.prnewswire.com/media/2096093/Twinkly_Logo_Logo.jpg)

# Twinkly Home Assistant Integration *(Unofficial)*

This is a custom integration for Home Assistant to control Twinkly Generation II lights using the `ttls` library.

## Installation

### Via HACS (Home Assistant Community Store)

1. Ensure HACS is installed in your Home Assistant setup.
2. In HACS, go to the Integrations section.
3. Click on the three dots in the top right corner and select "Custom repositories".
4. Add the repository URL: `https://github.com/air720boarder/twinkly-homeassistant` and select "Integration" as the category.
5. Search for "Twinkly Home Assistant Integration" and install it.
6. Restart Home Assistant.

### Manual Installation

1. Download the `twinkly_homeassistant` folder from the `custom_components` directory in this repository.
2. Place the `twinkly_homeassistant` folder into your Home Assistant's `custom_components` directory.
3. Restart Home Assistant.

## Configuration

1. After installation and restart, go to **Settings > Devices & Services > Add Integration**.
2. Search for **Twinkly Home Assistant Integration**.
3. Follow the setup wizard to add your Twinkly devices.

## Features

- Auto-discovery of Twinkly devices on your network.
- Control power, brightness, color, and effects.
- Supports multiple Twinkly devices.
- Local polling for status updates.

## Supported Languages

This integration includes translations for the following languages:

- **English**
- **Spanish (Español)**
- **French (Français)**
- **German (Deutsch)**
- **Italian (Italiano)**
- **Dutch (Nederlands)**
- **Portuguese (Português)**
- **Japanese (日本語)**
- **Chinese (Simplified and Traditional)**
- **Arabic (العربية)**
- **Russian (Русский)**
- **Hebrew (עברית)**
- **Polish (Polski)**
- **Swedish (Svenska)**
- **Norwegian (Norsk Bokmål)**
- **Finnish (Suomi)**
- **Danish (Dansk)**
- **Korean (한국어)**
- **Turkish (Türkçe)**
- **Czech (Čeština)**
- **Slovak (Slovenčina)**
- **Ukrainian (Українська)**
- **Hindi (हिन्दी)**

## Issues

If you encounter any issues, please report them on the [GitHub Issues](https://github.com/air720boarder/twinkly-homeassistant/issues) page.

## License

This project is licensed under the MIT License.

## Credit

This project heavily leverages the `ttls` library, which is a Python library for controlling Twinkly Generation II lights. [TTLS Github](https://github.com/jschlyter/ttls).

## HACS Installation

1. Add this repository to HACS as a custom repository.
2. Search for **Twinkly Home Assistant Integration** in HACS and install it.
3. Restart Home Assistant.
4. Twinkly devices should be auto-discovered. If not, you can add them manually via **Settings > Devices & Services > Add Integration**.