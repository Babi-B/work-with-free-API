
import os
import sys

import requests
from requests.adapters import HTTPAdapter
# import pandas as pd
# import matplotlib as mtp
from urllib3 import Retry

# sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import public

URL = "https://api.weather.gov/gridpoints/LOX/146,44/forecast/hourly"
HEADER = ["STARTTIME", "TEMPERATURE"]

def create_session():
    max_tries = Retry (
        total=4,
        backoff_factor=2,
        status_forcelist=public.STATUS_FORCE_LIST
        )
    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=max_tries))
    session.headers.update(
        {
            "accepts":"application/json",
            "User-Agent": public.USER_AGENT
        }
    )
    return session

def fetch_api(session):
    data = {}
    try:
        response = session.get(URL)
        records = response.json()["properties"]["periods"]
        for record in records:
            data[record["startTime"]] = record['temperature']
        return data
    except requests.HTTPError as e:
        print(f"Error: {e}")

def write_data(data):
    pass

def plot_data():
    pass

session = create_session()
print(fetch_api(session))