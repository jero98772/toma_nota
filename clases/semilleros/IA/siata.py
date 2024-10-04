import requests
import json
from datetime import datetime
import pytz
import polars as pl
import pandas as pd
# Constants
REQUEST_TIMEOUT = 5000  # Adjust timeout as needed
 
# Source information
source = {
    "url": "http://siata.gov.co/",
    "adapter": "medellin",
    "name": "Medellin",
    "city": "Medellin",
    "country": "CO",
    "description": "Sistema de Alerta Temprana de Medellín y el Valle de Aburrá - SIATA",
    "sourceURL": "http://siata.gov.co/",
    "contacts": [
        "info@openaq.org"
    ],
    "active": True
}
 
# Fetches data for a given source
def fetch_stream(source):
    pollutants = ['co', 'no2', 'ozono', 'pm10', 'pm25', 'so2']
    for pollutant in pollutants:
        yield fetch_pollutant_data(source['url'], pollutant)
 
# Fetches data for a specific pollutant
def fetch_pollutant_data(base_url, pollutant):
    url = f"{base_url}EntregaData1/Datos_SIATA_Aire_AQ_{pollutant}_Last.json"
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT / 1000)
        if response.status_code == 200:
            data = response.json()
            return [extract_measurements(item) for item in data['measurements']]
        else:
            print(f"Failed to fetch data for {pollutant}, status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error for {pollutant}: {e}")
    return []
 
# Extract specific fields from measurements
def extract_measurements(features):
    o = {
        'city': features['city'],
        'attribution': [features['attribution']],
        'value': features['value'],
        'location': features['location'],
        'date': format_date(features['date']['utc']),
        'averagingPeriod': {
            'unit': features['averagingPeriod']['units']
        },
        'coordinates': features['coordinates'],
        'parameter': features['parameter'] if features['parameter'] != 'pm10³' else 'pm10',
        'unit': features['unit'],
        'mobile': features['mobile']
    }
    return o
 
# Format date and time to UTC and local formats
def format_date(utc_date_str):
    tz = pytz.timezone('America/Bogota')
    utc_date = datetime.strptime(utc_date_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    local_date = utc_date.astimezone(tz)
    return {
        'utc': utc_date,
        'local': local_date.strftime('%Y-%m-%dT%H:%M:%S.%f')
    }

# Function to extract required data from JSON
def extract_data(data):
    if not isinstance(data, dict):
        raise ValueError(f"Expected a dictionary but got {type(data)}")
    
    # Process the data assuming it's in the correct format
    # Example: extract 'location', 'coordinates', 'value', etc.
    return {
        "location": data.get("location"),
        "latitude": data.get("coordinates", {}).get("latitude"),
        "longitude": data.get("coordinates", {}).get("longitude"),
        "pm25": data.get("value"),
        "parameter": data.get("parameter")
    }


import pandas as pd
import json

def main():
    try:
        dataframes_list = []
        
        for pollutant_data in fetch_stream(source):
            for data in pollutant_data:
                print(json.dumps(data, indent=4, default=str))  # Debug: Print raw JSON
                
                if isinstance(data, dict):  # Ensure data is a dictionary
                    records = extract_data(data)
                    
                    # Create Pandas DataFrame
                    df = pd.DataFrame([records])  # Wrap records in a list for single-row DataFrame
                    
                    # Cast columns to float where necessary
                    df["latitude"] = df["latitude"].astype(float)
                    df["longitude"] = df["longitude"].astype(float)
                    df["pm25"] = df["pm25"].astype(float)
                    
                    dataframes_list.append(df)
                else:
                    print(f"Warning: Expected dict, got {type(data)}")

        if dataframes_list:
            final_df = pd.concat(dataframes_list, ignore_index=True)
            final_df = final_df[final_df["pm25"] > 1024]

            print(f"Total rows: {len(final_df)}")
            print(final_df)
        else:
            print("No data found.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
 