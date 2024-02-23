"""
This code snippet contains three test functions for the `fetch_data_from_api` function
 in the `utility` module. 

The `test_fetch_data_from_api_successful` function tests the case where the API request
 is successful and the expected data is returned. It uses the `patch` function 
 from the `unittest.mock` module to mock the `requests.get` function and set the return values. 
 The expected data is defined and compared with the actual data returned 
 by the `fetch_data_from_api` function.

The `test_fetch_data_from_api_failure` function tests the case where the API request fails 
and no data is returned. It also uses the `patch` function to mock the `requests.get` function 
and set the return status code to 404. The actual data returned 
by the `fetch_data_from_api` function is compared with `None`.

The `test_fetch_data_from_api_exception` function tests the case where an exception occurs 
during the API request. It uses the `patch` function to mock the `requests.get` function and 
raise a `requests.RequestException` with a custom error message. The actual data returned 
by the `fetch_data_from_api` function is compared with `None`.

These test functions ensure that the `fetch_data_from_api` function behaves correctly in 
different scenarios and handle errors appropriately.
"""
from unittest.mock import patch
from utils import utility

import requests

def test_fetch_data_from_api_successful():
    """Test for checking successful API call"""
    api_url = "https://jsonplaceholder.typicode.com/users"
    expected_data = [{"id": 1, "name": "John Doe", "email": "john.doe@example.com"}]

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = expected_data

        actual_data = utility.fetch_data_from_api(api_url)

    assert actual_data == expected_data

def test_fetch_data_from_api_failure():
    """Test in case of failure in data fetching from API"""
    api_url = "https://jsonplaceholder.typicode.com/users"

    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = 404

        actual_data = utility.fetch_data_from_api(api_url)

    assert actual_data is None

def test_fetch_data_from_api_exception():
    """Tests API data fetch functionality"""
    api_url = "https://jsonplaceholder.typicode.com/users"

    with patch('requests.get', side_effect=requests.RequestException("Connection error")):
        actual_data = utility.fetch_data_from_api(api_url)

    assert actual_data is None
