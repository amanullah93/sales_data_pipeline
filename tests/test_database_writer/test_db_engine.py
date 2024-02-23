"""
This code snippet is a pytest test function that tests the 'write_to_database' function. 
It uses a fixture called 'sample_data' to generate sample data for testing. 
The test function calls the 'write_to_database' function to write the sample data to SQLite database. 
It then checks if the database file is created, if the tables are created, 
and if data is written to the tables. Finally, it cleans up by removing the created database file.

The purpose of this test function is to ensure that the 'write_to_database' function 
correctly writes data to the database and creates the necessary tables.
"""
from pathlib import Path
import sqlite3
import pandas as pd

from sqlalchemy import create_engine, inspect
from database_writer.db_engine import write_to_database

import pytest


@pytest.fixture
def sample_data():
    """Sample data for testing"""
    data = {
        'order_id': [1, 2, 3],
        'customer_id': [101, 102, 103],
        'product_id': [201, 202, 203],
        'quantity': [2, 3, 1],
        'price': [10, 20, 15],
        'order_date': ['2022-01-01', '2022-01-02', '2022-01-03'],
        'lat': [40.7128, 34.0522, 41.8781],
        'lng': [-74.0060, -118.2437, -87.6298],
        'temp': [25, 18, 22],
        'temp_min': [20, 15, 18],
        'temp_max': [30, 25, 25],
        'pressure': [1010, 1005, 1012],
        'humidity': [50, 60, 55],
        'wind_speed': [10, 8, 12],
        'wind_deg': [180, 200, 220],
        'weather_condition': ['Clear', 'Cloudy', 'Partly Cloudy'],
        'name': ['John', 'Alice', 'Bob'],
        'user_name': ['john_doe', 'alice_smith', 'bob_jones'],
        'email': ['john@example.com', 'alice@example.com', 'bob@example.com'],
        'store_id': [1, 2, 3],
        'store_name': ['Store A', 'Store B', 'Store C']
    }
    return pd.DataFrame(data)

def test_write_to_database(sample_data):
    """Call the function to write data to the database"""
    write_to_database(sample_data)

    # Check if the database file is created
    assert Path("internal_database.db").is_file()

    # Check if the tables are created
    engine = create_engine('sqlite:///internal_database.db')
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    assert 'orders' in tables
    assert 'customers' in tables
    assert 'products' in tables
    assert 'weather' in tables
    assert 'stores' in tables
    assert 'order_store_mapping' in tables

    # Check if data is written to the tables
    conn = sqlite3.connect('internal_database.db')
    df_from_db = pd.read_sql_query('SELECT * FROM orders', conn)
    assert not df_from_db.empty

    # Clean up: Remove the created database file
    Path("internal_database.db").unlink()
