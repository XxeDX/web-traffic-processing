# Simple Website Traffic Analysis Script

This Python script (web traffic processing.py) is designed to read website traffic data from an Apache access log in CSV format, clean and transform the data, calculate basic traffic metrics, and save the processed data into a local SQLite database. It includes basic error handling to ensure the process runs smoothly.

## Features

- **Data Cleaning and Transformation:**
  - Handles missing values by removing incomplete rows.
  - Converts timestamp strings to `datetime` objects.
  - Categorizes traffic sources as Direct, Search, or Referral based on the referrer.
  - Identify user's browsing platform.

- **Metrics Calculation:**
  - Calculates total page views.
  - Breaks down traffic by source (Direct, Search, Referral).

- **Database Storage:**
  - Saves the cleaned and processed data into a local SQLite database.

- **Error Handling:**
  - Integrated logging and error handling to capture and report issues during data processing.

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.x
- pandas
- sqlalchemy
- user_agents

##Sample data can be found in the sample data folder, which contains 500 rows of random generated data.
