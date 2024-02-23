-- Table for Orders
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price DECIMAL(10, 2),
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id),
);

-- Table for Customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    user_name TEXT,
    email TEXT
);

-- Table for Products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT
);

-- Table for Weather
CREATE TABLE weather (
    weather_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    lat FLOAT,
    lng FLOAT,
    temp FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    pressure INTEGER,
    humidity INTEGER,
    wind_speed FLOAT,
    wind_deg INTEGER,
    weather_condition TEXT
);

Table for Stores
CREATE TABLE stores (
    store_id INTEGER PRIMARY KEY,
    name TEXT,
    lat FLOAT,
    lng FLOAT
);

Table for Order-Store mapping
CREATE TABLE order_store_mapping (
    order_id INTEGER,
    store_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (store_id) REFERENCES stores(store_id),
    PRIMARY KEY (order_id, store_id)
);