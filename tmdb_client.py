import json
from ssl import ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE
import requests
list_to_choose = [{'popular':'Popular'}, {'upcoming':'Upcoming'}, {'now_playing': 'Now Playing'}, {'top_rated':'Top Rated'}]
api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmNWE0ODAwNjAyYWNhZmQyOTk1NzQyNTUyNjQwNjUxYyIsInN1YiI6IjYyNGRiMDM2MTg4NjRiMDBhMTcwMjdmMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.eD3iQwps65PMH2kf7ua8KbqWpFVXabq8zgZ5jY4KoUU"

def call_tmdb_api(endpoint):
   full_url = f"https://{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()

def get_movies_list(list_type):
   return call_tmdb_api(f"api.themoviedb.org/3/movie/{list_type}")

def get_popular_movies():
    return call_tmdb_api(f"api.themoviedb.org/3/movie/popular")

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_single_movie(movie_id):
    return call_tmdb_api(f"api.themoviedb.org/3/movie/{movie_id}")

def get_searched_movies(search_query):
    return call_tmdb_api(f"api.themoviedb.org/3/search/movie?query={search_query}")

def get_searched_series():
    return call_tmdb_api(f"api.themoviedb.org/3/tv/airing_today")


