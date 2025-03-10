# Movie Collection App

This is a Flask web application for managing a collection of movies. It allows users to add, edit, and delete movies from the collection.

## Features

- Add new movies to the collection
- Edit movie details such as rating and review
- Delete movies from the collection
- Display a list of all movies in the collection

## Technologies Used

- Flask
- Flask-Bootstrap
- Flask-SQLAlchemy
- Flask-WTF
- SQLite

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/movie-collection-app.git
    cd movie-collection-app
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the application:
    ```sh
    python main.py
    ```

5. Open your web browser and go to `http://127.0.0.1:5000/` to see the application.

## File Structure

- `main.py`: The main Flask application file.
- `templates/`: Directory containing HTML templates.
  - `index.html`: Template for displaying the list of movies.
  - `edit.html`: Template for editing movie details.
  - `add.html`: Template for adding new movies.
- `static/`: Directory containing static files (e.g., CSS, JavaScript).
- `requirements.txt`: List of required Python packages.

## Routes

- `/`: Home page displaying the list of movies.
- `/edit/<int:movie_id>`: Page for editing movie details.
- `/delete/<int:movie_id>`: Route for deleting a movie.
- `/add`: Page for adding a new movie.

## Models

- `Movie`: SQLAlchemy model representing a movie in the collection.

## Forms

- `EditForm`: WTForm for editing movie details.
- `AddForm`: WTForm for adding new movies.

## License

This project is licensed under the MIT License.
