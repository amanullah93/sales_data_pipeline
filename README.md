# Sales Data Transformation and Analysis Pipeline

## Overview

This Python script demonstrates a data transformation and analysis pipeline for sales data. It fetches user data from the JSONPlaceholder API, merges it with sales data, incorporates weather data from the OpenWeatherMap API, performs data manipulations and aggregations, and stores the transformed data in a relational database. Additionally, the script provides bonus features such as visualizations and Dockerization.

## Instructions

### Prerequisites

1. Python 3.x installed.
2. Required Python packages installed: `pandas`, `requests`, `matplotlib`, `sqlalchemy`, `pyyaml`, `pytest`.
   ```bash
   pip install pandas requests matplotlib sqlalchemy pyyaml
3. Replace 'OPEN_WEATHER_API_KEY' in the script with your actual OpenWeatherMap API key.
4. Run the script:
   ```bash
   python main.py

### Database
1. A SQLite database (`internal_database.db`) will be created to store the transformed data.

### Bonus Features
Visualizations

1. The script generates visualizations to present insights derived from the data.

### Dockerization
1. Create a Docker image
   ``` bash 
   docker build -t sales-data-pipeline .
2. Run the Docker container:
   ``` bash
   docker run -d --name sales-data-container sales-data-pipeline

