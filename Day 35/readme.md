# Weather Checker

This is a Python script that fetches the current weather data for a specific location using the OpenWeatherMap API and prints a message based on whether it is likely to rain or not.

## Features

- Fetches current weather data from the OpenWeatherMap API.
- Prints a message suggesting to bring an umbrella if precipitation is likely.
- Prints a message indicating clear skies if no precipitation is expected.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the `main.py` file.
2. Install the `requests` library if you haven't already:

    ```sh
    pip install requests
    ```

3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) by signing up for a free account.

4. Set the API key as an environment variable:

    - On Windows:

        ```sh
        setx weather_api_key "YOUR_API_KEY"
        ```

    - On macOS/Linux:

        ```sh
        export weather_api_key="YOUR_API_KEY"
        ```

## Usage

1. Ensure you have set the API key as an environment variable.
2. Run the `main.py` script:

    ```sh
    python main.py
    ```

3. The script will print the status code of the API response and a message based on the weather condition:
    - "Bring an umbrella" if precipitation is likely.
    - "Clear skies ahead" if no precipitation is expected.

## Code Explanation

- The script imports the necessary libraries: `requests` for making HTTP requests and `os` for accessing environment variables.
- It retrieves the API key from the environment variables.
- It defines the API endpoint and the parameters for the API request, including the latitude and longitude of the location.
- It sends a GET request to the OpenWeatherMap API with the specified parameters.
- It prints the status code of the API response to check if the request was successful.
- It parses the JSON response from the API into a Python dictionary.
- It checks the weather condition code:
  - If the weather condition code is less than 700, it prints "Bring an umbrella".
  - Otherwise, it prints "Clear skies ahead".

## License

This project is licensed under the MIT License.
