import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from datetime import datetime
import logging
from user_agents import parse

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to clean and transform the data
def clean_and_transform_data(df):
    try:
        # Handle missing values
        df.dropna(inplace=True)
        
        # Convert timestamp to datetime object
        df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%b/%Y:%H:%M:%S')
        
        # Extract relevant fields for analysis (referrer source, user platform)
        df['source'] = df['referrer'].apply(determine_source)

        df['platform'] = df['user_agent'].apply(determine_machine)
        
        logging.info("Data cleaning and transformation successful.")
        return df
    
    except Exception as e:
        logging.error(f"Error during data cleaning and transformation: {e}")
        raise

# Function to determine traffic source
def determine_source(referrer):
    if referrer == '-' or referrer is None:
        return 'Direct'
    elif 'google.com' in referrer or 'bing.com' in referrer or 'yahoo.com' in referrer:
        return 'Search'
    else:
        return 'Referral'

# Function to determine traffic source
def determine_machine(user_agent):
    user_agent_str = parse(user_agent)
    
    platform = user_agent_str.os.family
    
    return platform

# Function to calculate basic metrics
def calculate_metrics(df):
    try:
        metrics = {
            'total_page_views': df.shape[0],
            'traffic_sources': df['source'].value_counts().to_dict()
        }
        logging.info(f"Metrics calculated: {metrics}")
        return metrics
    
    except Exception as e:
        logging.error(f"Error during metrics calculation: {e}")
        raise

# Function to save data to SQLite
def save_to_database(df, db_name='web_traffic.db', table_name='traffic_data'):
    try:
        # Connect to SQLite database
        engine = create_engine(f'sqlite:///{db_name}', echo=False)
        
        # Save to database
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        
        logging.info(f"Data successfully saved to database {db_name} in table {table_name}.")
        
    except Exception as e:
        logging.error(f"Error saving data to database: {e}")
        raise

# Main function to process the data
def process_web_traffic_data(csv_file):
    try:
        # Read CSV file
        df = pd.read_csv(csv_file, names=['ip', 'timestamp', 'request', 'status', 'size', 'referrer', 'user_agent'], skiprows=1, engine='python')
        
        # Clean and transform the data
        df = clean_and_transform_data(df)
        
        # Save the processed data to a SQLite database
        save_to_database(df)
        
        return df
        
    except Exception as e:
        logging.error(f"Error processing web traffic data: {e}")
        raise

if __name__ == "__main__":
    # Main
    csv_file = 'apache_access_log.csv'  # Replace with the csv file path

    #Process and store to databse
    web_traffic_data = process_web_traffic_data(csv_file)

    #Print processed data
    with pd.option_context('display.max_rows', 10, 'display.max_columns', None):
        print(web_traffic_data)

    # Calculate and display metrics
    metrics = calculate_metrics(df)
    
    print(metrics)
