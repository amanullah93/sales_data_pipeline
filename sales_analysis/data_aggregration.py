"""
This module contains several functions for analyzing sales data using pandas and matplotlib.

total_sales_per_customer(df):
    Calculates the total sales for each customer in the given DataFrame and 
    saves a bar chart showing the total sales for each customer.

average_product_quantity(df):
    Calculates the average quantity of each product in the given DataFrame and 
    saves a bar chart showing the average product quantity for each product.

top_selling_product(df):
    Finds the top selling product in the given DataFrame based on the total quantity sold and 
    saves the product ID.

top_purchasing_customers(df):
    Finds the top purchasing customer in the given DataFrame based on the total sales and 
    saves the customer ID.

sales_trend(df):
    Calculates the total sales for each day, month, and year in the given DataFrame and 
    saves line charts showing the sales trend over time.

weather_trend(df):
    Calculates the total sales for each weather condition in the given DataFrame and 
    saves a bar chart showing the sales trend for each weather condition.
"""
import pandas as pd
import matplotlib.pyplot as plt


def total_sales_per_customer(df):
    """Calculates the total sales for each customer in the given DataFrame and 
    saves a bar chart showing the total sales for each customer."""
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("customer_id")["total_sales"].sum()
    ax = plt.subplot()
    total_sales_df.plot(x="customer_id", y="total_sales", kind="bar", ax=ax, 
                        title="Customer Total Sales")
    plt.savefig('total_sales_per_customer.png')
    plt.show()

def average_product_quantity(df):
    """Calculates the average quantity of each product in the given DataFrame and 
    saves a bar chart showing the average product quantity for each product."""
    average_product_quantity_df = df.groupby("product_id")["quantity"].mean()
    ax = plt.subplot()
    average_product_quantity_df.plot(x="product_id", y="quantity", kind="bar", ax=ax, 
                                     title="Average Product Quantity")
    plt.savefig('average_product_quantity.png')
    plt.show()    


def top_selling_product(df):
    """Finds the top selling product in the given DataFrame based on the total quantity sold and 
    saves the product ID."""
    average_product_quantity_df = df.groupby("product_id")["quantity"].sum()
    average_product_df = average_product_quantity_df.to_frame().reset_index()
    top_products = average_product_df[average_product_df["quantity"] == 
                                      average_product_df["quantity"].max()].reset_index()
    ax = plt.subplot()
    ax.axis('off')
    ax.text(x=0.5, y=0.5, size=25, ha="center", s=f"Top Selling Product is {top_products['product_id'][0]}")
    plt.savefig('top_selling_product.png')
    plt.show()


def top_purchasing_customers(df):
    """Finds the top purchasing customer in the given DataFrame based on the total sales and 
    saves the customer ID."""
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("customer_id")["total_sales"].sum()
    top_customers_df = total_sales_df.to_frame().reset_index()
    top_customers = top_customers_df[top_customers_df["total_sales"] == 
                                     top_customers_df["total_sales"].max()].reset_index()
    ax = plt.subplot()
    ax.axis('off')
    ax.text(x=0.5, y=0.5, size=25, ha="center", s=f"Top Purchasing Customer is {top_customers['customer_id'][0]}")
    plt.savefig('top_purchasing_customers.png')
    plt.show()


def sales_trend(df):
    """Calculates the total sales for each day, month, and year in the given DataFrame and 
    saves line charts showing the sales trend over time."""
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("order_date")["total_sales"].sum()
    ax = plt.subplot()
    total_sales_df.plot(x="order_date", y="total_sales", kind="line", ax=ax, title="Sales Trend Daily")
    plt.savefig('sales_trend_daily.png')
    plt.show()

    df["order_date"] = pd.to_datetime(df["order_date"])
    total_sales_df = df.groupby(df.order_date.dt.month)["total_sales"].sum()
    ax1 = plt.subplot()
    total_sales_df.plot(x="order_date", y="total_sales", kind="line", ax=ax1, title="Sales Trend Monthly")
    plt.savefig('sales_trend_monthly.png')
    plt.show()

    total_sales_df = df.groupby(df.order_date.dt.year)["total_sales"].sum()
    ax1 = plt.subplot()
    total_sales_df.plot(x="order_date", y="total_sales", kind="line", ax=ax1, title="Sales Trend Yearly")
    plt.savefig('sales_trend_yearly.png')
    plt.show()


def weather_trend(df):
    """Calculates the total sales for each weather condition in the given DataFrame and 
    saves a bar chart showing the sales trend for each weather condition."""
    df["total_sales"] = df["quantity"] * df["price"]
    total_sales_df = df.groupby("weather_condition")["total_sales"].sum()
    ax = plt.subplot()
    total_sales_df.plot(x="weather_condition", y="total_sales", kind="bar", ax=ax, title="Weather Trend")
    plt.savefig('weather_trend.png')
    plt.show()
