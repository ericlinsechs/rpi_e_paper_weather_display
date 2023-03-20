# Raspberry Pi E-Paper Weather Display
  This project is a Raspberry Pi-based weather display that uses an E-Paper display to show the current weather conditions and a famous qoute. It uses the OpenWeatherMap API to retrieve weather data for a specified location and displays the information on a 7.5 inch E-Paper display.

  This project is based on [this repo](https://github.com/AbnormalDistributions/e_paper_weather_display).

  ## Requirements
  To use this project, you will need the following:

  - A Raspberry Pi (In my case I use Raspberry Pi Zero W)
  - A Waveshare 7.5 inch E-Paper display (other displays may work, but have not been tested)
  - Python 3.7 or higher
  - A free OpenWeatherMap API key
  - A microSD card with Raspberry Pi OS installed

  ## Installation
  To install the necessary dependencies for this project, run the following commands:
  ```bash
  sudo apt-get update
  sudo apt-get install python3-pip python3-pil python3-numpy
  pip3 install RPi.GPIO spidev requests
  ```
  Next, clone this repository:
  ```bash
  git clone https://github.com/ericlinsechs/rpi_e_paper_weather_display.git
  ```

  ## License
  - This project is licensed under the MIT License - see the LICENSE.md file for details.