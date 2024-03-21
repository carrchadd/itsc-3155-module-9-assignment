from src.repositories.movie_repository import get_movie_repository


movie_repository = get_movie_repository()
movie_repository.create_movie('Avengers', 'Anthony Russo', 5)
movie_repository.create_movie('Cars 2', 'John Lasseter', 7)

def test_get_movies_empty(test_app):
	response = test_app.get('/movies')

	data = response.data.decode('utf-8')

	assert response.status_code == 200
	assert '<h1 class="mt-5 text-center">No Movies To Display</h1>' not in data

def test_get_all_movies(test_app):
	response = test_app.get('/movies')

	data = response.data.decode('utf-8')

	assert response.status_code == 200
	assert '<td>Avengers</td>' in data
	assert '<td>Anthony Russo</td>' in data
	assert '<td>5</td>' in data
	assert '<td>Cars 2</td>' in data
	assert '<td>John Lasseter</td>' in data
	assert '<td>7</td>' in data