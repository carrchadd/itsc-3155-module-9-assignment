# TODO: Feature 4
from src.repositories.movie_repository import get_movie_repository

def test_get_movie_by_id():
    movie_repository = get_movie_repository()

    test_movie_id = 1

    retrieved_movie = movie_repository.get_movie_by_id(test_movie_id)

    assert retrieved_movie.movie_id == test_movie_id