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

api_key = "991151555f8ce4e8e419b86588278595"
location = "Taoyuan City"
lat = '24.992901'
lon = '121.300972'
city_id = "6696918"
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
    
    # display.draw_text(550, 160, weather.current_timestamp(), font130, black)
    
    ###################################################################################################################
    # CURRENT WEATHER
    display.draw_icon(570, 40, "b", 120, 120,
                      weather.weather_description(weather.current_weather())[0])  # CURRENT WEATHER ICON
    display.draw_text(580, 140, weather.weather_description(weather.current_weather())[1], font70, black)
    # display.draw_black.text((310, 130), weather.current_temp(), font=font100, fill=black)
    display.draw_text(350, 10, weather.current_temp(), font130, black)
    #display.draw_black.text((30, 400), weather.current_temp_min() + " - " + weather.current_temp_max(), font=font35, fill=black)
    display.draw_text(350, 140, "H:" + forecast.today_temp_max() + " L:" + forecast.today_temp_min(), font70, black)
    
    display.draw_black.text((100, 250), quote.quote_string()[0], font=quote_font40, fill=black)
    display.draw_text(350, 400, quote.quote_string()[1], quote_font30, black)
    # display.draw_black.text((320, 230), "H:" + weather.current_temp_max(), font=font35, fill=black)
    # display.draw_text(420, 230, "L:" + weather.current_temp_min(), font50, black)
   
    # display.draw_icon(400, 150, "b", 35, 35, "feels_temp")
    # display.draw_text(550, 5, "Feels Like", font50, black)
    # display.draw_icon(530, 70, "b", 65, 65, weather.current_feels_like_icon())
    # display.draw_black.text((400, 200), weather.current_feels_like(), font=font35, fill=black)
    # display.draw_black.text((30, 390), weather.current_hum(), font=font35, fill=black)
    # display.draw_black.text((30, 390), weather.current_pressure(), font=font35, fill=black)

    # display.draw_icon(160, 30, "b", 50, 50, "sunrise")  # SUNRISE ICON
    # display.draw_text(180, 75, weather.current_sunrise(), font40, black)
    # display.draw_icon(230, 30, "b", 50, 50, "sunset")  # SUNSET ICON
    # display.draw_text(250, 75, weather.current_sunset(), font40, black)
    
    # display.draw_text(700, 120, "Air QUALITY", font50, black)
    # display.draw_icon(680, 185, "b", 65, 65, pollution.current_air_quality())

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
