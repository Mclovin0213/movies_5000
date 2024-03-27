import pandas as pd

CSV_PATH = 'tmdb_5000_movies.csv'

data = pd.read_csv(CSV_PATH)

data = data.drop(['production_companies', 'production_countries', 
           'spoken_languages', 'tagline', 'overview', 'original_language', 
           'original_title', 'keywords', 'homepage'], axis=1)

data = data[data['status'] != 'Rumored']
data = data[data['status'] != 'Post Production']
data = data[data['vote_count'] >= 100]

data.to_csv('cleaned_data.csv', index=False)

