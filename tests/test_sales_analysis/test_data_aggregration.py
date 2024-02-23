"""
This code snippet is a test module for the functions total_sales_per_customer, 
average_product_quantity, top_selling_product, top_purchasing_customers, sales_trend, 
and weather_trend. It uses the pytest framework for testing.

The sample_sales_data fixture provides a sample DataFrame for testing the functions.

The test_total_sales_per_customer function tests the total_sales_per_customer function 
by calling it with the sample_sales_data DataFrame and checking 
if the PNG file "total_sales_per_customer.png" is generated.

The test_average_product_quantity function tests the average_product_quantity function 
by calling it with the sample_sales_data DataFrame and checking 
if the PNG file "average_product_quantity.png" is generated.

The test_top_selling_product function tests the top_selling_product function by calling it 
with the sample_sales_data DataFrame and checking if the PNG file "top_selling_product.png" is generated.

The test_top_purchasing_customers function tests the top_purchasing_customers function 
by calling it with the sample_sales_data DataFrame and checking if the PNG file "top_purchasing_customers.png" is generated.

The test_sales_trend function tests the sales_trend function by calling it with the 
sample_sales_data DataFrame and checking if the PNG files "sales_trend_daily.png", 
"sales_trend_monthly.png", and "sales_trend_yearly.png" are generated.

The test_weather_trend function tests the weather_trend function by calling it 
with the sample_sales_data DataFrame and checking if the PNG file "weather_trend.png" is generated.
"""

from pathlib import Path
import pandas as pd
from sales_analysis.data_aggregration import (
    total_sales_per_customer,
    average_product_quantity,
    top_selling_product,
    top_purchasing_customers,
    sales_trend,
    weather_trend,
)

import pytest


@pytest.fixture
def sample_sales_data():
    """Sample sales data for testing"""
    data = {
        "customer_id": [1, 2, 1, 3, 2],
        "product_id": [101, 102, 101, 103, 104],
        "quantity": [2, 3, 1, 4, 2],
        "price": [10, 20, 15, 8, 25],
        "order_date": [
            "2022-01-01",
            "2022-01-01",
            "2022-01-02",
            "2022-01-02",
            "2022-01-03",
        ],
        "weather_condition": ["Sunny", "Rainy", "Sunny", "Snowy", "Rainy"],
    }
    return pd.DataFrame(data)


def test_total_sales_per_customer(sample_sales_data):
    """Check if the PNG file is generated"""
    total_sales_per_customer(sample_sales_data)
    assert Path("total_sales_per_customer.png").is_file()


def test_average_product_quantity(sample_sales_data):
    """Check if the PNG file is generated"""
    average_product_quantity(sample_sales_data)
    assert Path("average_product_quantity.png").is_file()


def test_top_selling_product(sample_sales_data):
    """Check if the PNG file is generated"""
    top_selling_product(sample_sales_data)
    assert Path("top_selling_product.png").is_file()


def test_top_purchasing_customers(sample_sales_data):
    """ Check if the PNG file is generated"""
    top_purchasing_customers(sample_sales_data)
    assert Path("top_purchasing_customers.png").is_file()


def test_sales_trend(sample_sales_data):
    """ Check if the PNG files are generated"""
    sales_trend(sample_sales_data)
    assert Path("sales_trend_daily.png").is_file()
    assert Path("sales_trend_monthly.png").is_file()
    assert Path("sales_trend_yearly.png").is_file()


def test_weather_trend(sample_sales_data):
    """ Check if the PNG file is generated"""
    weather_trend(sample_sales_data)
    assert Path("weather_trend.png").is_file()
