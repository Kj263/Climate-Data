import json
import requests

def filter_data(start_year, end_year, country):
    response = requests.get('https://kj263.github.io/Climate-Data/GCB_percapita.json')
    records = response.json()
    
    filtered = [
        record for record in records
        if (start_year <= int(record['Year']) <= end_year) and (country.lower() in record['Country'].lower())
    ]
    
    with open('filtered_data.json', 'w') as f:
        json.dump(filtered, f)

if __name__ == "__main__":
    filter_data(2000, 2024, 'USA')  # Example usage
