# -*- coding: utf-8 -*-

# import forecastio
# from geopy.geocoders import Nominatim


# api_key = "31fa9e666ed5ad3d3511e188e7c4d143"
# latitude = 38.627003
# longitude = -90.199402

# forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()

# print("{} and {}".format(forecast.summary, forecast.temperature))

# def get_weather(latitude, longitude, api_key):
# 	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
# 	return "{} and {} ".format(forecast.summary, forecast.temperature)


# print(get_weather(latitude, longitude, api_key))

# geolocator = Nominatim()
# location = geolocator.geocode("McCarren Park")
# print(location.address)

# location = geolocator.geocode("McCarren Park, NYC")
# print(location.address)

# print(location.longitude)
# print(location.raw)


import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
    api_key = os.environ['FORECASTIO_API_KEY']
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    latitude = location.latitude
    longitude = location.longitude
    forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
    summary = forecast.summary
    temperature = forecast.temperature
    return "{} and {}° at {}".format(summary, temperature, address)
	


