  # Raspberry Pi E-Paper Weather Display
  This project is a weather display built using a Raspberry Pi and an ePaper display. The display shows current weather conditions, forecast, and current temperature trends. It also features a famous qoute display.

  ![end_product](./photos/end_product.jpg)
  ## Requirements
  To use this project, you will need the following:

  - A Raspberry Pi (In my case I use Raspberry Pi Zero W)
  - A Waveshare 7.5 inch E-Paper display (other displays may work, but have not been tested)
  - A microSD card with Raspberry Pi OS installed
  - 5 x 7" photo frame (i bought it from [IKEA](https://www.ikea.com/us/en/p/ribba-frame-black-50378448/))
  - Python 3.7 or higher
  - A free OpenWeatherMap API key

  ## Setup
  1. Connect the ePaper display to the Raspberry Pi according to the instructions provided by the manufacturer.
  2. Install the required software packages using pip.
  3. Clone this repository to your Raspberry Pi.
  4. Configure config.json file in your case.
  5. Run `sudo python3 main.py` to start the program.

  ## Configuration
  The program can be configured using the config.ini file. The following options are available:

  - api_key: Your OpenWeatherMap API key (register your own key from [here]( https://home.openweathermap.org/users/sign_up.)).
  - location: Your city.
  - city_id: Your city ID.
  - latitude: The latitude of your location (get it from [here](https://www.latlong.net )).
  - longitude: The longitude of your location (get it from [here](https://www.latlong.net )).
  - units: The unit system to use (imperial or metric).
  ## Credits
  This project is based on the [ePaper Weather Display](https://github.com/AbnormalDistributions/e_paper_weather_display).
  ## License
  - This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.