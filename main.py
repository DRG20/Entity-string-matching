"""
Uses Companies House API to obtain real-time information on UK company registry 

The module contains a function called download_data(), which takes an API key 
as an argument and downloads the latest data from the API using the requests 
library.

@author: Cozma Dragos
"""
import os
from utils.companies_house import *

if __name__ == "__main__":
    # Prompt the user to enter their API key
    api_key = input("Please enter your Companies House API key: ")

    # Set the API key as an environment variable
    os.environ["COMPANIES_HOUSE_API_KEY"] = api_key

    # Download data from the Companies House API
    download_data()