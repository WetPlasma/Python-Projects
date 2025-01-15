# Exercise Tracker

This script uses the Nutritionix API to track exercises and their details such as name, duration, and calories burned.

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

1. Set up your Nutritionix API credentials in the `main.py` file:
    ```python
    # Nutritionix API
    App_Id = "your_app_id"
    App_Key = "your_app_key"
    ```

2. Replace `"your_app_id"` with your Nutritionix App ID.
3. Replace `"your_app_key"` with your Nutritionix App Key.

## Usage

Run the script using Python:
```sh
python main.py
