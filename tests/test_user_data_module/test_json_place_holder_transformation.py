"""
This code snippet contains a set of unit tests for the functions `parse_user_data`, 
`merge_sales_and_user_data`, `fetch_sales_data`, and `fetch_user_data`. 

The `parse_user_data` function takes a list of user data obtained from an API and 
returns a list of dictionaries with specific user information. 

The `merge_sales_and_user_data` function merges user data and sales data 
based on a common key and returns the merged dataframe. 

The `fetch_sales_data` function reads sales data from a CSV file and returns a dataframe. 

The `fetch_user_data` function fetches user data from an API, parses it, and returns a dataframe. 

The unit tests ensure that these functions are working correctly by 
comparing the expected output with the actual output. 
"""
from unittest.mock import patch
import pandas as pd

from user_data_module.json_place_holder_transformation import parse_user_data, merge_sales_and_user_data, fetch_sales_data, fetch_user_data

import pytest

@pytest.fixture
def sample_user_data():
    """Sample user data"""
    return [
        {
            "id": 1,
            "name": "John Doe",
            "username": "john_doe",
            "email": "john@example.com",
            "address": {"geo": {"lat": 40.7128, "lng": -74.0060}}
        },
        {
            "id": 2,
            "name": "Alice Smith",
            "username": "alice_smith",
            "email": "alice@example.com",
            "address": {"geo": {"lat": 34.0522, "lng": -118.2437}}
        }
    ]

@pytest.fixture
def sample_sales_data():
    """Sample sales data"""
    data = {
        "customer_id": [1, 2, 3],
        "order_id": [101, 102, 103],
        "product_id": [201, 202, 203],
        "quantity": [2, 3, 1],
        "price": [10, 20, 15]
    }
    return pd.DataFrame(data)

@pytest.fixture
def sample_merged_data():
    """Sample data for testing"""
    data = {
        "customer_id": [1, 2],
        "order_id": [101, 102],
        "product_id": [201, 202],
        "quantity": [2, 3],
        "price": [10, 20],
        "name": ["John Doe", "Alice Smith"],
        "user_name": ["john_doe", "alice_smith"],
        "email": ["john@example.com", "alice@example.com"],
        "lat": [40.7128, 34.0522],
        "lng": [-74.0060, -118.2437]
    }
    return pd.DataFrame(data)

def test_parse_user_data(sample_user_data):
    """Parses the user data for further processing"""
    parsed_users = parse_user_data(sample_user_data)
    assert len(parsed_users) == 2
    assert parsed_users[0]["customer_id"] == 1
    assert parsed_users[1]["user_name"] == "alice_smith"

def test_merge_sales_and_user_data(sample_sales_data, sample_user_data, sample_merged_data):
    """Merges sales and user data"""
    merged_df = merge_sales_and_user_data(pd.DataFrame(sample_user_data), sample_sales_data, "customer_id")
    pd.testing.assert_frame_equal(merged_df, pd.DataFrame(sample_merged_data))

def test_fetch_sales_data(tmp_path):
    """Fetches sales data"""
    file_path = tmp_path / "sales_data.csv"
    sample_sales_data = {
        "customer_id": [1, 2, 3],
        "order_id": [101, 102, 103],
        "product_id": [201, 202, 203],
        "quantity": [2, 3, 1],
        "price": [10, 20, 15]
    }
    pd.DataFrame(sample_sales_data).to_csv(file_path, index=False)

    fetched_data = fetch_sales_data(file_path)
    pd.testing.assert_frame_equal(fetched_data, pd.DataFrame(sample_sales_data))

def test_fetch_user_data(sample_user_data):
    """This function fetches user data"""
    with patch('data_module.utility.fetch_data_from_api', return_value=sample_user_data):
        fetched_data = fetch_user_data("http://example.com/api/users")
        assert len(fetched_data) == 2
        assert fetched_data["user_name"].tolist() == ["john_doe", "alice_smith"]
