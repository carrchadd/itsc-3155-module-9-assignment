from app import app

def test_edit_movie_page():
    test_app = app.test_client()

    response = test_app.get('/movies/1/edit')

    assert response.status_code == 200
    assert b'<label for="title" class="form-label">Title</label>' in response.data