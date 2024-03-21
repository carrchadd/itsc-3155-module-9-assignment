import pytest
from app import app
from src.repositories.movie_repository import get_movie_repository

@pytest.fixture()
def test_app():
	return app.test_client()
	
	
def test_all_movies_page(test_app):
	response = test_app.get('/movies')
	assert response.status_code == 200
