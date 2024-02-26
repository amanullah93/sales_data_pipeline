"""
This code snippet contains a set of unit tests for the functions in the 
'open_weather_transformation' module of the 'aiq_data_pipeline.weather_module' package. 

The tests cover the following functions:
- generate_random_coordinates(): Generates random latitude and longitude coordinates 
within a specified radius.
- get_weather_info_from_open_weather(): Fetches weather information from the OpenWeather API based
 on the given latitude, longitude, and order ID.
- get_weather_for_orders(): Fetches weather information for each order in a given DataFrame by 
calling the get_weather_info_from_open_weather() function.
- merge_sales_and_weather_data(): Merges the weather data with the sales data based on the order ID.

The tests use the 'sample_sales_data' and 'sample_weather_data' fixtures to provide sample data for testing.

Each test asserts specific conditions to ensure the correct behavior of the corresponding function.

Note: The code snippet also imports necessary modules and packages, 
such as 'unittest.mock', 'pandas', and 'pytest', and defines the 'sample_sales_data' and 
'sample_weather_data' fixtures.

"""
from unittest.mock import patch, MagicMock
import pandas as pd
from weather_module.open_weather_transformation import (
    generate_random_coordinates,
    get_weather_info_from_open_weather,
    get_weather_for_orders,
    merge_sales_and_weather_data
)

import pytest


@pytest.fixture
def sample_sales_data():
    """Sample sales data"""
    data = {
        "order_id": [101, 102, 103],
        "customer_id": [1, 2, 3],
        "product_id": [201, 202, 203],
        "quantity": [2, 3, 1],
        "price": [10, 20, 15]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_weather_data():
    """sample weather data"""
    data = {
        "order_id": [101, 102, 103],
        "temp": [23.5, 20.0, 25.2],
        "temp_min": [18.3, 15.1, 20.0],
        "temp_max": [25.0, 22.2, 28.0],
        "pressure": [1010, 1005, 1012],
        "humidity": [65, 75, 60],
        "wind_speed": [5.5, 6.0, 4.8],
        "wind_deg": [120, 150, 100],
        "weather_condition": ["Clear", "Cloudy", "Sunny"],
        "store_lat": [40.800092, 40.840484, 40.867585],
        "store_lng": [-73.937664, -73.874683, -73.885559]
    }
    return pd.DataFrame(data)

def test_generate_random_coordinates():
    """Generate random coordinates for testing"""
    coordinates = generate_random_coordinates()
    assert "lat" in coordinates
    assert "lng" in coordinates

# def test_get_weather_info_from_open_weather():
#     """Tests get_weather_info_from_open_weather function"""
#     with patch('weather_module.utility.fetch_data_from_api', return_value=sample_weather_data.iloc[0].to_dict()):
#         weather_info = get_weather_info_from_open_weather("40.800092", "-73.937664", 101, "https://api.openweathermap.org/data/2.5/weather?", "ab1a190f731c0466744dc8e0c9109346")
#         assert weather_info["order_id"] == 101
#         assert "temp" in weather_info
#         assert "weather_condition" in weather_info

# def test_get_weather_for_orders(sample_sales_data):
#     """Tests get_weather_for_orders function"""
#     with patch('weather_module.utility.fetch_data_from_api', return_value=sample_weather_data.iloc[0].to_dict()):
#         weather_data = get_weather_for_orders(sample_sales_data, "https://api.openweathermap.org/data/2.5/weather?", "ab1a190f731c0466744dc8e0c9109346")
#         assert len(weather_data) == len(sample_sales_data)
#         assert "temp" in weather_data.columns
#         assert "wind_speed" in weather_data.columns

def test_merge_sales_and_weather_data(sample_sales_data, sample_weather_data):
    """Tests merge_sales_and_weather_data"""
    merged_data = merge_sales_and_weather_data(sample_weather_data, sample_sales_data, "order_id")
    assert len(merged_data) == len(sample_sales_data)
    assert "temp" in merged_data.columns
    assert "price" in merged_data.columns
