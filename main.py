import pandas as pd

CSV_PATH = 'tmdb_5000_movies.csv'

data = pd.read_csv(CSV_PATH)

data.drop(['production_companies', 'production_countries', 
           'spoken_languages', 'tagline', 'overview', 'original_language', 
           'original_title', 'keywords', 'id', 'homepage'], axis=1)

for idx, status in enumerate(data['status']):
    if status == 'Rumored':
        data['status'].drop(idx)
        print('dropped!')

# print(data.head())
print(data['tagline'])

