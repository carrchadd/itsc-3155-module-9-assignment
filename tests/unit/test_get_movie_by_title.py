# TODO: Feature 3
from flask.testing import FlaskClient 
from src.repositories.movie_repository import get_movie_repository
import pytest

def test_get_movie_by_title_empty(test_app:FlaskClient):
    response = test_app.get('/movies/search')
    assert response.status_code == 200