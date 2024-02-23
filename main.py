"""
Module providing main function to execute data pipeline.

This module contains functions that execute different steps of a data pipeline. 
The pipeline includes fetching user and sales data from JSON placeholder, merging the data, 
fetching weather data for the orders, merging the weather data with the sales data, 
performing various data aggregations, and writing the final data to a database.

Functions:
- execute_json_place_holder_transformation: Fetches user and sales data from a JSON placeholder, 
merges the data, and returns the merged dataframe.
- execute_open_weather_transformation: Fetches weather data for the orders, merges the weather data 
with the sales data, and returns the final merged dataframe.
- execute_data_aggregation: Performs various data aggregations on the final merged dataframe.
- write_to_database: Writes the final merged dataframe to a database.
- execute_data_pipeline: Executes the entire data pipeline by calling the above functions 
in required order.

"""
import logging
import yaml

from user_data_module import json_place_holder_transformation
from weather_module import open_weather_transformation
from sales_analysis import data_aggregration
from database_writer import db_engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.info("main module execution started")

with open("config.yaml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)

# Access the variable value
USER_API_URL = config["USER_API_URL"]
SALES_DATA_FILE_NAME = config["SALES_DATA_FILE_NAME"]
SALES_MERGE_KEY = config["SALES_MERGE_KEY"]
OPEN_WEATHER_API_URL = config["OPEN_WEATHER_API_URL"]
OPEN_WEATHER_API_KEY = config["OPEN_WEATHER_API_KEY"]
ORDER_MERGE_KEY = config["ORDER_MERGE_KEY"]

def execute_json_place_holder_transformation():
    """Fetches user and sales data from JSON placeholder,merges the data 
    and returns the merged dataframe."""
    user_df = json_place_holder_transformation.fetch_user_data(USER_API_URL)
    sales_df = json_place_holder_transformation.fetch_sales_data(SALES_DATA_FILE_NAME)
    merged_df = json_place_holder_transformation.merge_sales_and_user_data(
        user_df, sales_df, SALES_MERGE_KEY)
    logger.info("user_data_module execution completed")
    return merged_df


def execute_open_weather_transformation(merged_df):
    """Fetches weather data for the orders, merges the weather data 
    with the sales data, and returns the final merged dataframe."""
    weather_df = open_weather_transformation.get_weather_for_orders(
        merged_df, OPEN_WEATHER_API_URL, OPEN_WEATHER_API_KEY)
    final_df = open_weather_transformation.merge_sales_and_weather_data(
        weather_df, merged_df, ORDER_MERGE_KEY )
    logger.info("weather_module execution completed")
    return final_df


def execute_data_aggregation(final_df):
    """Performs various data aggregations on the final merged dataframe."""
    data_aggregration.total_sales_per_customer(final_df)
    data_aggregration.average_product_quantity(final_df)
    data_aggregration.top_selling_product(final_df)
    data_aggregration.top_purchasing_customers(final_df)
    data_aggregration.sales_trend(final_df)
    data_aggregration.weather_trend(final_df)
    logger.info("sales_analysis module execution completed")



def write_to_database(final_df):
    """Writes the final merged dataframe to a database."""
    db_engine.write_to_database(final_df)
    logger.info("database_write module execution completed")


def execute_data_pipeline():
    """Executes the entire data pipeline by calling the below functions 
    in required order."""
    merged_df = execute_json_place_holder_transformation()
    final_df = execute_open_weather_transformation(merged_df)
    execute_data_aggregation(final_df)
    write_to_database(final_df)


if __name__ == "__main__":
    execute_data_pipeline()
    logger.info("main module execution completed")
