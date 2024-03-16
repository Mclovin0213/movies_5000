import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMBD_API")

url = "https://api.themoviedb.org/3/movie/129/images"

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)

print(response.text)