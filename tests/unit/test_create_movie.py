# TODO: Feature 2
from src.repositories.movie_repository import get_movie_repository

movie_repository = get_movie_repository()

def test_create_movie():
    initial_movie_count = len(movie_repository.get_all_movies())
    movie_repository.create_movie('Test Movie', 'Test Director', 4)
    updated_movie_count = len(movie_repository.get_all_movies())
    assert updated_movie_count == initial_movie_count + 1