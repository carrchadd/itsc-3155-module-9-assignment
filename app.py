from flask import Flask, redirect, render_template, request

from src.repositories.movie_repository import get_movie_repository

app = Flask(__name__)

# Get the movie repository singleton to use throughout the application
movie_repository = get_movie_repository()

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    movie_db = movie_repository.get_all_movies();
    length = len(movie_db)
    return render_template('list_all_movies.html', movies=movie_db, len=length, list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.route('/movies', methods = ['POST'])
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    title = request.form.get('title')
    director = request.form.get('director')
    rating = int(request.form.get('rating'))

    movie_duplicate = movie_repository.get_movie_by_title(title)

    if movie_duplicate:
        return redirect('/movies')
    
    if rating < 1 or rating > 5:
        return redirect('/movies')

    movie_repository.create_movie(title, director, rating)
    return redirect('/movies')


@app.route('/movies/search', methods=['GET', 'POST'])
def search_movies():
    # TODO: Feature 3
    if request.method == 'POST':
        title = request.form.get('title')
        movie = movie_repository.get_movie_by_title(title)
        if movie:
            results = [movie]
            return render_template('search_movies.html', search_active=True, results=results)
        else:
            return render_template('search_movies.html', search_active=True, not_found=True)
    else: 
        return render_template('search_movies.html', search_active=True)


@app.get('/movies/<int:movie_id>')
def get_single_movie(movie_id: int):
    # TODO: Feature 4
    movie = movie_repository.get_movie_by_id(movie_id)
    return render_template('get_single_movie.html', movie = movie)


@app.get('/movies/<int:movie_id>/edit')
def get_edit_movies_page(movie_id: int):
    movie = movie_repository.get_movie_by_id(movie_id)

    if movie is None:
        return "Movie not found", 404
    
    return render_template('edit_movies_form.html', movie=movie)


@app.post('/movies/<int:movie_id>')
def update_movie(movie_id: int):
    title = request.form['title']
    director = request.form['director']
    rating = int(request.form['rating'])

    try:
        movie = movie_repository.update_movie(movie_id, title, director, rating)
        return redirect('/movies')
    except ValueError as e:
        return str(e), 404


@app.route('/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(movie_id: int):
    old_movie = movie_repository.get_movie_by_id(movie_id)
    if not old_movie:
        raise ValueError(f'movie with id {movie_id} not found')
    movie_repository.delete_movie(movie_id)
    # Remove the movie from the dictionary (or any other data store you're using)
    return redirect('/movies')
