import pandas as pd

CSV_PATH = 'cleaned_data.csv'

movies = pd.read_csv(CSV_PATH)

def get_top_100_movies(movies):
    # Sort movies by vote_average and drop columns that are not needed
    sorted_movies = movies.sort_values(by='vote_average', ascending=False)
    sorted_movies = sorted_movies.drop(columns=[col for col in sorted_movies.columns if col not in ['title', 'vote_average', 'id', 'release_date', 'vote_count']])
    
    # Drop movies with less than 100 votes
    sorted_movies = sorted_movies[sorted_movies['vote_count'] > 100]

    return sorted_movies.head(100)

