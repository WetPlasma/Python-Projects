# Pixela User Creation Script

This script creates a new user on the Pixela service using the provided API endpoint and parameters.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the `main.py` file.
2. Install the required Python library using pip:
    ```sh
    pip install requests
    ```

## Configuration

1. Set up your Pixela user creation parameters in the `main.py` file:
    ```python
    pixela_endpoint = "https://pixe.la/v1/users"

    params = {
        "token": "thisisatoken",
        "username": "thisisusername52",
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }
    ```

2. Replace `"thisisatoken"` with your desired token.
3. Replace `"thisisusername52"` with your desired username.

## Usage

Run the script using Python:
```sh
python main.py
