"""
This module defines a function called fetch_data_from_api that takes an API URL as input and 
returns the data fetched from the API. 

Parameters:
- api_url (str): The URL of the API to fetch data from.

Returns:
- data (dict): The JSON data fetched from the API.

If the request to the API is successful (status code 200), the function parses the JSON data 
from the response and returns it. If the request fails or encounters an exception, 
an error message is printed and None is returned.

"""
import logging
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def fetch_data_from_api(api_url):
    """This function takes an API URL as input and returns the data fetched from the API. """
    try:
        response = requests.get(api_url, timeout=120)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            data = response.json()
            return data
        else:
            logger.info("Error: Unable to fetch data from the API. Status code: %s", response.status_code)
            return None
    except requests.RequestException as e:
        logger.error("Error: %s", e)
        return None
    