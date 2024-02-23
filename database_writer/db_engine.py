"""
This module defines a function called write_to_database that takes a DataFrame as input and 
writes its contents to a SQLite database. The function creates several tables in the database, 
including 'orders', 'customers', 'products', 'weather', 'stores', and 'order_store_mapping'. 

Each table corresponds to a subset of columns from the input DataFrame. 
The function uses the SQLAlchemy library to create an engine for connecting to the database and 
then uses the to_sql method of the DataFrame to write the data to the respective tables. 
If a table with the same name already exists in the database, it is replaced. 
The database file is named 'internal_database.db' and is assumed to be located in the 
current working directory.
"""
from sqlalchemy import create_engine


def write_to_database(df):
    """This function takes a DataFrame as input and writes its contents to a SQLite database."""
    database_name = 'internal_database.db'
    engine = create_engine(f'sqlite:///{database_name}')

    df['store_id'] = df['order_id']
    # Create tables
    df_orders = df[['order_id', 'customer_id', 'product_id', 'quantity', 'price', 'order_date']]
    df_customers = df[['customer_id', 'name', 'user_name', 'email']]
    df_products = df[['product_id', 'name']]
    df_weather = df[
        ['order_id', 'lat', 'lng', 'temp', 'temp_min', 'temp_max', 'pressure', 'humidity', 
         'wind_speed', 'wind_deg', 'weather_condition']]
    df_stores = df[['store_id', 'name', 'lat', 'lng']]
    df_order_store_mapping = df[['order_id', 'store_id']]

    # Store DataFrames into tables
    df_orders.to_sql('orders', con=engine, index=False, if_exists='replace')
    df_customers.to_sql('customers', con=engine, index=False, if_exists='replace')
    df_products.to_sql('products', con=engine, index=False, if_exists='replace')
    df_weather.to_sql('weather', con=engine, index=False, if_exists='replace')
    df_stores.to_sql('stores', con=engine, index=False, if_exists='replace')
    df_order_store_mapping.to_sql('order_store_mapping', con=engine, index=False, if_exists='replace')
