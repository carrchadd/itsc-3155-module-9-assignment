# TODO: Feature 4
from app import app

def test_view_movie_page():
    test_app = app.test_client()

    response = test_app.get('/movies/1')

    assert response.status_code == 200
    assert b'<h1 class="display-3">Avengers: Endgame</h1>' in response.data