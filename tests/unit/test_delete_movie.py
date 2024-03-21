# TODO: Feature 6
def test_delete_movie(client):
    # Create a sample movie
    response = client.post('/movies', json={'title': 'Inception', 'director': 'Christopher Nolan', 'rating': 5})
    assert response.status_code == 201

    # Get the movie ID from the response
    movie_id = response.json['id']

    # Delete the movie
    response = client.delete(f'/movies/{movie_id}')
    assert response.status_code == 200
    assert response.json['message'] == f'Movie "Inception" deleted successfully'

    # Verify that the movie is no longer in the database
    response = client.get(f'/movies/{movie_id}')
    assert response.status_code == 404