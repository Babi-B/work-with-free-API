# Version 2: Create a session first
import requests
from requests.adapters import HTTPAdapter
from urllib3 import Retry

# const
URL = "https://catfact.ninja/fact"
STATUS_LIST = [
    408,  # Request Timeout
    422,  # Unprocessable Content (Validation failed, or endpoint spammed)
    429,  # Too Many Requests
    500,  # Internal Server Error
    502,  # Bad Gateway
    503,  # Service Unavailable
    504,  # Gateway Timeout
]


def create_session():
    max_retries = Retry(
        total=3,
        backoff_factor=2,
        status_forcelist=STATUS_LIST
    )

    session = requests.Session()
    session.mount("https://", HTTPAdapter(max_retries=max_retries))
    return session

def fetch_fact(session):
    try:
        response = session.get(URL) 
        response.raise_for_status()         
        data = response.json()
        return data.get("fact", [])
    except requests.RequestException as e:
        print(f"Error Detected {e}")

session = create_session()
data = fetch_fact(session)

print(data)

