import time
import datetime
import requests

class Weather:
    def __init__(self, latitude, longitude, api_key, city_id, units):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key
        self.city_id = city_id
        self.units = units
        self.data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={self.city_id}&appid={self.api_key}&units={self.units}").json()
        pass

    def update(self):
        self.data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?id={self.city_id}&appid={self.api_key}&units={self.units}").json()
        return self.data

    def current_time(self):
        return time.strftime("%d/%m/%Y %H:%M", time.localtime(self.data["dt"]))

    def current_date(self):
        return time.strftime("%m/%d", time.localtime(self.data["dt"]))
    
    def current_weekday(self):        
        return time.strftime("%A", time.localtime(self.data["dt"]))
    
    def current_timestamp(self):        
        return time.strftime("%H:%M", time.localtime(self.data["dt"]))
    
    def current_temp(self):
        return "{:.0f}".format(self.data["main"]["temp"]) + u"\N{DEGREE SIGN}C"

    def current_temp_min(self):
        return "{:.0f}".format(self.data["main"]["temp_min"]) + u"\N{DEGREE SIGN}"
        
    def current_temp_max(self):
         return "{:.0f}".format(self.data["main"]["temp_max"]) + u"\N{DEGREE SIGN}"
    
    def current_feels_like(self):
        return "{:.0f}".format(self.data["main"]["feels_like"]) + u"\N{DEGREE SIGN}C"
    
    def current_feels_like_icon(self):
        deg = self.data["main"]["feels_like"]
        icon_name = ""
        if deg > 26:
            icon_name = "hot_feeling"
        elif deg <= 26 and deg >= 20:
            icon_name = "comfy_feeling"
        elif deg < 20:
            icon_name = "cold_feeling"
        return icon_name

    def current_hum(self):
        return "{:.0f}".format(self.data["main"]["humidity"]) + "%"

    def current_pressure(self):
        return "{:.0f}".format(self.data["main"]["pressure"]) + "hPa"

    def current_cloud_cov(self):
        return "{:.0f}".format(self.data["clouds"]) + "%"

    def current_sunrise(self):
        return time.strftime("%H:%M", time.localtime(self.data["sys"]["sunrise"]))

    def current_sunset(self):
        return time.strftime("%H:%M", time.localtime(self.data["sys"]["sunset"]))

    def current_wind(self):
        deg = self.data["wind"]["deg"]
        if deg < 30 or deg >= 330:
            direction = "N"
        elif 30 <= deg < 60:
            direction = "NE"
        elif 60 <= deg < 120:
            direction = "E"
        elif 120 <= deg < 150:
            direction = "SE"
        elif 150 <= deg < 210:
            direction = "S"
        elif 210 <= deg < 240:
            direction = "SO"
        elif 240 <= deg < 300:
            direction = "O"
        elif 300 <= deg < 330:
            direction = "NO"
        else:
            direction = "N/A"
        return "{:.0f}".format(self.data["wind"]["speed"]) + "km/h", direction

    def current_weather(self):
        description = self.data["weather"][0]["id"]
        return description
    def weather_description(self, id):
        icon = "sun"
        weather_detail = "Beau temps"
        if id // 100 != 8 and id // 100 != 5:
            id = id // 100
            if id == 2:
                icon = "thunder"
                weather_detail = "thunderstorm"
            elif id == 3:
                icon = "drizzle"
                weather_detail = "drizzle"
            elif id == 6:
                icon = "snow"
                weather_detail = "snow"
            elif id == 7:
                icon = "atm"
                weather_detail = "mist"
            else:
                weather_detail = "error"
        else:
            if id == 800:
                icon = "sun"
                weather_detail = "clear sky"
            elif id == 801:
                icon = "25_clouds"
                weather_detail = "few clouds"
            elif id == 802:
                icon = "50_clouds"
                weather_detail = "scattered clouds"
            elif id == 803 or id == 804:
                icon = "100_clouds"
                weather_detail = "overcast"
            elif id == 500 or id == 501:
                icon = "rain"
                weather_detail = "rain"
            elif id >= 503 and id <= 531:
                icon = "heavy_rain"
                weather_detail = "heavy rain"

        return icon, weather_detail
    
class Forecast:
    def __init__(self, latitude, longitude, api_key, city_id, units):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key
        self.city_id = city_id
        self.units = units
        self.data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?id={self.city_id}&appid={self.api_key}&units={self.units}").json()
        pass
    def update(self):
        self.data = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?id={self.city_id}&appid={self.api_key}&units={self.units}").json()
        return self.data
    
    def today_temp_max(self):
        temp_max = 0
        hr = time.strftime("%H", time.localtime(self.data["list"][0]["dt"]))
        left_hr = 24 - int(hr) 
        if left_hr < 3:
            return "{:.0f}".format(self.data["list"][0]["main"]["temp_max"]) + u"\N{DEGREE SIGN}"
        else:
            index = left_hr//3
            for i in range(index):
                if temp_max < self.data["list"][i]["main"]["temp_max"]:
                    temp_max = self.data["list"][i]["main"]["temp_max"]
        return "{:.0f}".format(temp_max) + u"\N{DEGREE SIGN}"
        
    def today_temp_min(self):
        temp_min = 100
        hr = time.strftime("%H", time.localtime(self.data["list"][0]["dt"]))
        left_hr = 24 - int(hr)
        
        if left_hr < 3:
            return "{:.0f}".format(self.data["list"][0]["main"]["temp_min"]) + u"\N{DEGREE SIGN}"
        else:
            index = left_hr//3
            for i in range(index):
                if temp_min > self.data["list"][i]["main"]["temp_min"]:
                    temp_min = self.data["list"][i]["main"]["temp_min"]
        return "{:.0f}".format(temp_min) + u"\N{DEGREE SIGN}"
class Pollution:
    def __init__(self, latitude, longitude, api_key, city_id, units):
        self.latitude = latitude
        self.longitude = longitude
        self.api_key = api_key
        self.data = requests.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}").json()
        pass
    def update(self):
        self.data = requests.get(f"https://api.openweathermap.org/data/2.5/air_pollution?lat={self.latitude}&lon={self.longitude}&appid={self.api_key}").json()
        return self.data
    def current_air_quality(self):
        aqi = self.data["list"][0]["main"]["aqi"]
        air_quality = ""
        if aqi == 1:
            air_quality = "good"
        elif aqi == 2 or aqi == 3:
            air_quality = "moderate"
        elif aqi == 4:
            air_quality = "poor"
        elif aqi == 5:
            air_quality = "very_poor"
        return air_quality
    
