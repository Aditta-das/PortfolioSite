import requests
from bs4 import BeautifulSoup
import re, json


class Scrap:
	def __init__(self, query):
		self.query = query


	def api_call(self):
		with open("weather_api.txt", "r") as f:
			api_key = f.read()
			openweather = f"http://api.openweathermap.org/data/2.5/weather?q={self.query}&appid={api_key}"
			json_data = requests.get(openweather).json()	
			temp_ = json_data["main"]["temp"]

			temp_cel = int(temp_ - 273.15)
			main_ = json_data["weather"]
			day_type = "".join([d["main"] for d in main_])

			wind_ = json_data["wind"]["speed"]
			humidity_ = json_data["main"]["humidity"]
			icon = json_data["weather"][0]["icon"]
			location = json_data["name"]
			country_name = json_data["sys"]["country"]
			return temp_cel, day_type, wind_, humidity_, location, country_name, icon


print(Scrap("dhaka").api_call())