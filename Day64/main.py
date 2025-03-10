from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Optional
import requests
import sqlite3

app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap(app)

# Updated database name
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///D:\Shreyas\python tutorials\MovieSql\movies1.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(1000), nullable=False)


class form(FlaskForm):
    title = StringField("Title")  # No validators so it's optional
    year = IntegerField("Year", validators=[Optional()])
    description = StringField("Description")
    rating = IntegerField("Rating", validators=[Optional()])
    ranking = IntegerField("Ranking", validators=[Optional()])
    review = StringField("Review")
    img_url = StringField("Image URL")

    submit = SubmitField("Submit")


# Create database and add a dummy movie only once
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.ranking).all()

    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:movie_id>", methods=["GET", "POST"])
def edit(movie_id):
    movie = Movie.query.get(movie_id)  # Correct usage  # Find movie by ID
    if not movie:
        return redirect(url_for("home"))

    edit_form = form(obj=movie)  # Prefill form with movie data

    if edit_form.validate_on_submit():
        # Only update fields with new values, keeping previous values otherwise
        movie.title = edit_form.title.data if edit_form.title.data else movie.title
        movie.year = (
            edit_form.year.data if edit_form.year.data is not None else movie.year
        )
        movie.description = (
            edit_form.description.data
            if edit_form.description.data
            else movie.description
        )
        movie.rating = (
            edit_form.rating.data if edit_form.rating.data is not None else movie.rating
        )
        movie.ranking = (
            edit_form.ranking.data
            if edit_form.ranking.data is not None
            else movie.ranking
        )
        movie.review = edit_form.review.data if edit_form.review.data else movie.review
        movie.img_url = (
            edit_form.img_url.data if edit_form.img_url.data else movie.img_url
        )

        db.session.commit()
        return redirect(url_for("home"))

    return render_template("edit.html", form=edit_form, movie=movie)


@app.route("/delete/<int:movie_id>")
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    if movie_to_delete:
        db.session.delete(movie_to_delete)
        db.session.commit()

    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    add_form = form()

    if add_form.validate_on_submit():
        new_movie = Movie(
            title=add_form.title.data,
            year=add_form.year.data,
            description=add_form.description.data,
            rating=add_form.rating.data,
            ranking=add_form.ranking.data,
            review=add_form.review.data,
            img_url=add_form.img_url.data,
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("add.html", form=add_form)


if __name__ == "__main__":
    app.run(debug=True)
