# Cafe Collection API

This is a Flask web application for managing a collection of cafes. It allows users to add, edit, and delete cafes from the collection.

## Features

- Add new cafes to the collection
- Edit cafe details such as name, location, and amenities
- Delete cafes from the collection
- Display a list of all cafes in the collection

## Technologies Used

- Flask
- Flask-SQLAlchemy
- SQLite

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/cafe-collection-api.git
    cd cafe-collection-api
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
  - `index.html`: Template for displaying the list of cafes.
- `requirements.txt`: List of required Python packages.

## API Endpoints

- `GET /cafes`: Retrieve a list of all cafes.
- `POST /cafes`: Add a new cafe.
- `PATCH /cafes/<int:cafe_id>`: Update details of a specific cafe.
- `DELETE /delete/<int:cafe_id>`: Delete a specific cafe (requires API key).

## Models

- `Cafe`: SQLAlchemy model representing a cafe in the collection.

## Example Requests

### Get All Cafes

```sh
curl -X GET http://127.0.0.1:5000/cafes
