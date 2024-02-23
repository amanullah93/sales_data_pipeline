"""
This module includes several functions for fetching weather information 
from the OpenWeather API and merging it with sales data.

Functions:
- generate_random_coordinates(): Generates random latitude and longitude coordinates 
within a specified radius.
- get_weather_info_from_open_weather(lat, lng, order_id): Fetches weather information 
from the OpenWeather API based on the given latitude, longitude, and order ID.
- get_weather_for_orders(df): Fetches weather information for each order in a given DataFrame 
by calling the get_weather_info_from_open_weather() function.
- merge_sales_and_weather_data(weather_data, sales_data): Merges the weather data 
with the sales data based on the order ID.
"""
import logging

import random
import math
import pandas as pd

from utils import utility

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info(" weather module execution started")

def generate_random_coordinates():
    """Generates random latitude and longitude coordinates 
    within a specified radius."""
    radius = 1000000
    radius_in_degree = radius/111300
    x0 = 40.84
    y0 = -73.87
    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = radius_in_degree * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    y = w * math.sin(t)
    lat = round(x + x0, 6)
    lng = round(y + y0, 6)
    return {"lat": str(lat), "lng": str(lng)}


def get_weather_info_from_open_weather(lat, lng, order_id, open_weather_api_url, open_weather_api_key):
    """Fetches weather information from the OpenWeather API based on the 
    given latitude, longitude, and order ID."""
    url = f"{open_weather_api_url}lat={lat}&lon={lng}&appid={open_weather_api_key}"
    weather_info = utility.fetch_data_from_api(url)
    logger.info(" successfully fetched OPENWEATHERMAP API data")
    return {
        "order_id": order_id,
        "temp": weather_info["main"]["temp"],
        "temp_min": weather_info["main"]["temp_min"],
        "temp_max": weather_info["main"]["temp_max"],
        "pressure": weather_info["main"]["pressure"],
        "humidity": weather_info["main"]["humidity"],
        "wind_speed": weather_info["wind"]["speed"],
        "wind_deg": weather_info["wind"]["deg"],
        "weather_condition": weather_info["weather"][0]["description"],
        "store_lat": lat,
        "store_lng": lng
    }


def get_weather_for_orders(df, open_weather_api_url, open_weather_api_key):
    """Fetches weather information for each order in a given DataFrame 
    by calling the get_weather_info_from_open_weather() function."""
    weather_info = []
    for i in range(0, df.shape[0]):
        lat_lng = generate_random_coordinates()
        weather_info.append(
            get_weather_info_from_open_weather(lat_lng["lat"], lat_lng["lng"], df["order_id"][i],
                                               open_weather_api_url, open_weather_api_key)
        )
    return pd.DataFrame.from_dict(weather_info)


def merge_sales_and_weather_data(weather_data, sales_data, order_merge_key):
    """Merges the weather data with the sales data based on the order ID."""
    merged_df = sales_data.merge(weather_data, on=order_merge_key)
    return merged_df
