"""
This module includes several functions for fetching and processing data.

Functions:
- parse_user_data(users): Parses user data obtained from an API and 
returns a list of dictionaries with specific user information.
- merge_sales_and_user_data(user_data, sales_data): Merges user data and sales data 
based on a common key and returns the merged dataframe.
- fetch_sales_data(): Reads sales data from a CSV file and returns a dataframe.
- fetch_user_data(): Fetches user data from an API, parses it, and returns a dataframe.

Variables:
- USER_API_URL: The URL of the API to fetch user data from.
- SALES_DATA_FILE_NAME: The name of the CSV file containing sales data.
- sales_merge_key: The key to merge user data and sales data on.
"""
import logging

from utils import utility
import pandas as pd

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("user data module execution started")

def parse_user_data(users):
    """Parses user data obtained from an API and 
    returns a list of dictionaries with specific user information."""
    parsed_users = []
    for user in users:
        parsed_users.append({
            "customer_id": user["id"],
            "name": user["name"],
            "user_name": user["username"],
            "email": user["email"],
            "lat": user["address"]["geo"]["lat"],
            "lng": user["address"]["geo"]["lng"]
        })
    return parsed_users


def merge_sales_and_user_data(user_data, sales_data, sales_merge_key):
    """Merges user data and sales data 
    based on a common key and returns the merged dataframe."""
    merged_df = sales_data.merge(user_data, on=sales_merge_key)
    return merged_df


def fetch_sales_data(sales_data_file_name):
    """Reads sales data from a CSV file and returns a dataframe."""
    try:
        sales_df = pd.read_csv(sales_data_file_name)
        sales_df = sales_df.head(20)
        logger.info("sales data fetched successfully")
        return sales_df
    except FileNotFoundError as e:
        logger.error("Error: %s", e)
        return None


def fetch_user_data(user_api_url):
    """Fetches user data from an API, parses it, and returns a dataframe."""
    users = utility.fetch_data_from_api(user_api_url)
    parsed_users = parse_user_data(users)
    logger.info("user data fetch completed")
    return pd.DataFrame.from_dict(parsed_users)
