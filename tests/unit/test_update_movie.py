from src.repositories.movie_repository import get_movie_repository

def test_update_movie():
    movie_repository = get_movie_repository()

    test_movie_id = 1
    new_title = "New Title"
    new_director = "New Director"
    new_rating = 4

    updated_movie = movie_repository.update_movie(test_movie_id, new_title, new_director, new_rating)

    assert updated_movie.title == new_title
    assert updated_movie.director == new_director
    assert updated_movie.rating == new_rating

    retrieved_movie = movie_repository.get_movie_by_id(test_movie_id)

    assert retrieved_movie.title == new_title
    assert retrieved_movie.director == new_director
    assert retrieved_movie.rating == new_rating
