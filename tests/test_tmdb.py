import tmdb_client
from unittest.mock import Mock
from main import app
from tmdb_client import list_to_choose
import pytest
# zadanie chapter 14.3

@pytest.mark.parametrize('n, result', (
   ('popular', {'results': []}),
   ('top_rated', {'results': []}),
   ('upcoming', {'results': []}),
   ('now_playing', {'results': []})
))

def test_homepage(monkeypatch, n, result):
    api_mock = Mock()
    api_mock.return_value = result
    monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

    with app.test_client(n) as client:
        response = client.get(f'/?list_type={n}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(f"api.themoviedb.org/3/movie/{n}")


# zadanie chapter 14.2
def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']

    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list



def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = {"cast": ['Actor 1', 'Actor 2']}

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie_cast = tmdb_client.get_single_movie_cast(movie_id=675353)

    assert movie_cast == mock_movie_cast["cast"]

def test_get_single_movie(monkeypatch):
    mock_movie = ['Movie']

    requests_mock = Mock()
    response = requests_mock.return_value
    response.json.return_value = mock_movie
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

    movie = tmdb_client.call_tmdb_api(endpoint=675353)

    assert movie == mock_movie
