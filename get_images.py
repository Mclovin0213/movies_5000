import requests
import os
import pandas as pd
from dotenv import load_dotenv
from filter import get_top_100_movies
import time

load_dotenv()

API_KEY = os.getenv("TMBD_API")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

IMAGE_PATH = "assets/"

base_url = "http://image.tmdb.org/t/p/"

size = "original"

def get_posters(IDs):
    for id in IDs:
        url = f"https://api.themoviedb.org/3/movie/{id}/images?language=en"
        
        response = requests.get(url, headers=headers)
        
        data = response.json()
        
        image_source = data['posters'][0]['file_path']
        
        image_url = f"{base_url}{size}{image_source}"
        
        print(image_url)
        
        response = requests.get(image_url, headers=headers)
        
        if response.status_code == 200:
            
            new_path = f"{IMAGE_PATH}movie{id}.jpg"
            
            print(new_path)
            
            with open(new_path, "wb") as file:
                file.write(response.content)
                print(f"Image downloaded successfully and saved to {new_path}.")
        else:
            print("Failed to retrieve the image.")

        time.sleep(2)

data = pd.read_csv('cleaned_data.csv')

movie_100 = get_top_100_movies(data)

movie_IDs = movie_100['id'].tolist()

get_posters(movie_IDs)