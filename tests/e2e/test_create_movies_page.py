# TODO: Feature 2
from flask.testing import FlaskClient

def test_create_movie(test_app:FlaskClient):
    response = test_app.get('/movies')
    assert response.status_code == 200
    