# This little program is for the Waveshare 7.5
# inch Version 2 black and white only epaper display
# It uses OpenWeatherMap API to display weather info

from PIL import Image, ImageDraw, ImageFont
import json
import time
import traceback
from datetime import datetime
from waveshare_epd import epd7in5_V2

from weather import *
from display import *
from quotes import *


# Search lib folder for display driver modules
# sys.path.append('lib')
epd = epd7in5_V2.EPD()

# Update interval
sleep_seconds = 1800

# Set the colors
black = 'rgb(0,0,0)'
white = 'rgb(255,255,255)'
grey = 'rgb(235,235,235)'
red = 'rgb(255,0,0)'

update_date = 0

def main(display, weather, forecast, quote):        
    # Current date
    display.draw_text(100, 30, weather.current_date(), font100, 'black')
    display.draw_text(100, 100, weather.current_weekday(), font100, 'black')
    
    # Current weather
    display.draw_icon(570, 40, "b", 120, 120, weather.weather_description(weather.current_weather())[0])
    display.draw_text(580, 140, weather.weather_description(weather.current_weather())[1], font70, 'black')
    display.draw_text(350, 10, weather.current_temp(), font130, 'black')
    display.draw_text(350, 140, "H:" + forecast.today_temp_max() + " L:" + forecast.today_temp_min(), font70, 'black')
    
    # Quotes
    display.draw_black.text((100, 250), quote.quote_string()[0], font=quote_font40, fill='black')
    display.draw_text(350, 400, quote.quote_string()[1], quote_font30, 'black')

    # Display image
    time.sleep(2)
    epd.display(epd.getbuffer(display.background))
    time.sleep(2)
    
if __name__ == "__main__":
    # Load config data
    with open('config.json', 'r') as f:
        config = json.load(f)
    api_key = config['api_key']
    location = config['location']
    city_id = config['city_id']
    lat = config['lat']
    lon = config['lon']
    units = config['units']
     
    # Create display object
    epd = epd7in5_V2.EPD()
    epd.init()
    epd.Clear()
    display = Display()
    
    # Initialize weather, forecast, and quote objects
    weather = Weather(lat, lon, api_key, city_id, units)
    forecast = Forecast(lat, lon, api_key, city_id, units)
    pollution = Pollution(lat, lon, api_key, city_id, units)
    quote = Quote()
    
    # Set update interval
    sleep_seconds = 1800
    update_date = datetime.now().day
    
    while True:
        try:
            current_time = time.strftime("%d/%m/%Y %H:%M", time.localtime())
            print(f"Begin update at {current_time}")
            
            # Check if it's a new day and update forecast and quote
            if update_date != datetime.now().day:
                forecast.update()
                quote.update()
                update_date = datetime.now().day
                
            # Update display
            main(display, weather, forecast, quote)
             # Sleep until the next update
            print(f'Sleeping for {sleep_seconds/60} minutes...')
            epd.sleep()
            time.sleep(sleep_seconds)
            
        except Exception as e:
            print(f"UPDATE ERROR: {e}")
            traceback.print_exc()
            time.sleep(2)
