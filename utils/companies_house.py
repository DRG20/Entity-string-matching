"""
Uses Companies House API to obtain real-time information on UK company registry 

The module contains a function called download_data(), which takes an API key 
as an argument and downloads the latest data from the API using the requests 
library.

@author: Cozma Dragos
"""
import requests
import os

def download_data():
    # Get the API key from an environment variable
    api_key = os.environ.get("COMPANIES_HOUSE_API_KEY")

    # Define the URL for the Companies House API
    url = "https://api.companieshouse.gov.uk/search/companies"

    # Define the headers for the request, including the API key
    headers = {"Authorization": f"Basic {api_key}", "Accept": "application/json"}

    # Make the request to the API
    response = requests.get(url, headers=headers, params={})

    # Check the response status code
    if response.status_code == 200:
        # Save the response data to a file
        # By default this will be saved in the data folder for now
        with open("./data/companies_house_data.json", "wb") as f:
            f.write(response.content)
        print("Companies House data downloaded successfully!")
    else:
        print(f"Error downloading Companies House data: {response.status_code}")


