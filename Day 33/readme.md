# ISS Overhead Notifier

This Python script checks if the International Space Station (ISS) is currently overhead and if it is nighttime at your location. If both conditions are met, it sends an email notification.

## Features

- Checks the current position of the ISS.
- Determines if it is nighttime at your location.
- Sends an email notification if the ISS is overhead and it is nighttime.

## Requirements

- Python 3.x
- requests
- smtplib (included with Python)

## Installation

1. Clone the repository or download the code files.
2. Ensure you have the required library installed. You can install requests using pip:

    ```sh
    pip install requests
    ```

3. Update the `my_email` and `password` variables in the script with your email credentials.
4. Update the `MY_LAT` and `MY_LONG` variables with your latitude and longitude.

## Usage

1. Run the `main.py` script:

    ```sh
    python main.py
    ```

2. The script will check every minute if the ISS is overhead and if it is nighttime. If both conditions are met, it will send an email notification to the specified email address.

## Code Explanation

- The `iss_overhead` function checks the current position of the ISS and determines if it is within +5 or -5 degrees of your location.
- The `is_night` function checks the current time and determines if it is nighttime at your location based on sunrise and sunset times.
- The script runs an infinite loop that checks the conditions every minute and sends an email notification if the conditions are met.

## License

This project is licensed under the MIT License.
