![Twinkly logo](https://mma.prnewswire.com/media/2096093/Twinkly_Logo_Logo.jpg)

# Twinkly Home Assistant Integration *(Unofficial)*

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]
![Project Maintenance][maintenance-shield]

Home Assistant integration for Twinkly smart lights.

## Installation

### HACS (Recommended)

1. Install [HACS](https://hacs.xyz/)
2. Add this repository to HACS as a custom repository:
   - Click on HACS in the sidebar
   - Click on Integrations
   - Click the three dots in the top right corner
   - Select "Custom repositories"
   - Add the URL of this repository
   - Select "Integration" as the category
3. Click Install
4. Restart Home Assistant

### Manual Installation

1. Copy the `custom_components/twinkly` directory to your Home Assistant's `custom_components` directory
2. Restart Home Assistant

## Configuration

1. Go to Settings -> Devices & Services
2. Click "Add Integration"
3. Search for "Twinkly"
4. Follow the configuration steps

## Features

- Automatic discovery of Twinkly devices
- Support for on/off, brightness, and effects
- Real-time control and status updates

## Contributing

This project welcomes contributions and suggestions. Please fork the repository and submit a pull request with your changes.

[commits-shield]: https://img.shields.io/github/commit-activity/y/air720boarder/twinkly-homeassistant.svg
[commits]: https://github.com/air720boarder/twinkly-homeassistant/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg
[license-shield]: https://img.shields.io/github/license/air720boarder/twinkly-homeassistant.svg
[maintenance-shield]: https://img.shields.io/badge/maintainer-%40air720boarder-blue.svg
[releases-shield]: https://img.shields.io/github/release/air720boarder/twinkly-homeassistant.svg
[releases]: https://github.com/air720boarder/twinkly-homeassistant/releases