## Data Pipeline Execution

The `main.py` script calls the `execute_data_pipeline` function, which is responsible for executing a data pipeline by invoking four other functions: `execute_json_place_holder_transformation` `execute_open_weather_transformation`, `execute_data_aggregation` and `write_to_database`

### Inputs
1. Sales data CSV file
2. JSONPlaceholder API
3. OpenWeatherMap API

### Flow

1. The `execute_data_pipeline` function calls the `execute_json_place_holder_transformation` function.
2. The `execute_json_place_holder_transformation` function retrieves user data and sales data from a JSON placeholder API from `user_data_module`.
3. The retrieved data is merged into a single DataFrame.
4. Next, the `execute_data_pipeline` function calls the `execute_open_weather_transformation` function.
5. The `execute_open_weather_transformation` function reads the `OPENWEATHERMAP` API data as a dataframe
6. The weather data is merged with the `user_data_module` DataFrame.
8. Then we performed aggregation logics on the merged data in `sales_analysis` module.
9. Then, `execute_data_pipeline` calls the `execute_data_aggregation` function, which performs various data aggregation operations, such as calculating total sales per customer, average product quantity, top selling product, top purchasing customers, sales trend, and weather trend.


### Outputs
1. Finally, `execute_data_pipeline` calls the `write_to_database` function from `database_writer` module, which reads the final merged dataframe and writes the data to corresponding tables in a SQLite database.
