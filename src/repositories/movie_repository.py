
from src.models import db, movie

class MovieRepository:

    def get_all_movies(self):
        # TODO get all movies from the DB
        movies = movie.query.all()
        return movies

    def get_movie_by_id(self, movie_id):
        # TODO get a single movie from the DB using the ID
        return movie.query.filter_by(movie_id=movie_id).first()

    def create_movie(self, title, director, rating):
        # TODO create a new movie in the DB
        newMovie = movie(title=title,director=director,rating=rating)
        db.session.add(newMovie)
        db.session.commit()
        return newMovie

    def search_movies(self, title):
        # TODO get all movies matching case insensitive substring (SQL LIKE, use google for how to do with SQLAlchemy)
        title = f"%{title}%"
        foundMovies = movie.query.filter(movie.title.like(title)).all()
        return foundMovies


# Singleton to be used in other modules
movie_repository_singleton = MovieRepository()
