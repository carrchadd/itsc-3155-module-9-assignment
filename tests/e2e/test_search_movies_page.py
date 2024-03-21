# TODO: Feature 3
from flask.testing import FlaskClient 
from src.repositories.movie_repository import get_movie_repository


movie_repository = get_movie_repository()

# checking if movie repository is empty 
def test_get_movie_by_title_empty():
    assert movie_repository.get_movie_by_title('title') is None