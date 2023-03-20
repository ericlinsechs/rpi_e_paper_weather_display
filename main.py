# This little program is for the Waveshare 7.5
# inch Version 2 black and white only epaper display
# It uses OpenWeatherMap API to display weather info
from PIL import Image, ImageDraw, ImageFont
import json
import requests
from io import BytesIO
import traceback
import time
from datetime import datetime
from waveshare_epd import epd7in5_V2
import sys
import os

from weather import *
from display import *
from quotes import *

api_key = "Your API KEY"
location = "Your City"
lat = ''
lon = ''
city_id = "110204"
units = 'metric'

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
URL = BASE_URL + "id=" + city_id + "&appid=" + api_key + "&units=" + units

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

def main():        
    # Current date
    display.draw_text(100, 30, weather.current_date(), font100, black)
    display.draw_text(100, 100, weather.current_weekday(), font100, black)
    
    ###################################################################################################################
    # CURRENT WEATHER
    display.draw_icon(570, 40, "b", 120, 120, weather.weather_description(weather.current_weather())[0])  # CURRENT WEATHER ICON
    display.draw_text(580, 140, weather.weather_description(weather.current_weather())[1], font70, black)
    display.draw_text(350, 10, weather.current_temp(), font130, black)
    display.draw_text(350, 140, "H:" + forecast.today_temp_max() + " L:" + forecast.today_temp_min(), font70, black)
    
    display.draw_black.text((100, 250), quote.quote_string()[0], font=quote_font40, fill=black)
    display.draw_text(350, 400, quote.quote_string()[1], quote_font30, black)

    # display image
    time.sleep(2)
    epd.display(epd.getbuffer(display.background))
    time.sleep(2)
    
if __name__ == "__main__":
    while True:
        try:
            print('Connecting to Open Weather...')
            weather = Weather(lat, lon, api_key, city_id, units)
            forecast = Forecast(lat, lon, api_key, city_id, units)
            pollution = Pollution(lat, lon, api_key, city_id, units)
            quote = Quote()
            break
        except:
            # Call function to display connection error
            current_time = time.strftime("%d/%m/%Y %H:%M:%S", time.localtime())
            print("INITIALIZATION PROBLEM- @" + current_time)
            time.sleep(2)
    while True:
        # Defining objects
        current_time = time.strftime("%d/%m/%Y %H:%M", time.localtime())
        print("Begin update @" + current_time)
        print("Creating display")
        display = Display()
        # Update data
        weather.update()
        pollution.update()
        if (update_date != int(time.strftime("%d", time.localtime()))):
            update_date = int(time.strftime("%d", time.localtime()))
                 
            forecast.update()
            quote.update()
        print("Data Update complete!")
        print("Main program running...")
        epd.init()
        epd.Clear()
        main()
        print('Sleeping for ' + str((sleep_seconds/60)) + 'min...')
        epd.sleep()
        time.sleep(sleep_seconds)
