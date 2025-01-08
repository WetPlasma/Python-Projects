# Birthday Wisher

This is a Python script that automatically sends birthday wishes via email. The script reads a list of birthdays from a CSV file and sends a personalized birthday message to the person if their birthday is today.

## Features

- Reads birthday data from a CSV file.
- Selects a random birthday message template.
- Sends a personalized birthday email.

## Requirements

- Python 3.x
- pandas
- smtplib (included with Python)

## Installation

1. Clone the repository or download the code files.
2. Ensure you have the required library installed. You can install pandas using pip:

    ```sh
    pip install pandas
    ```

3. Create a CSV file named `birthdays.csv` with the following columns:
    - `name`
    - `email`
    - `year`
    - `month`
    - `day`

4. Create a directory named `letter_templates` and add text files named `letter_1.txt`, `letter_2.txt`, and `letter_3.txt` with your birthday message templates. Use `[NAME]` as a placeholder for the recipient's name.

5. Update the `MY_EMAIL`, `MY_PASSWORD`, and `YOUR EMAIL PROVIDER SMTP SERVER ADDRESS` variables in the script with your email credentials and SMTP server address.

## Usage

1. Run the `main.py` script:

    ```sh
    python main.py
    ```

2. If today matches any birthday in the `birthdays.csv` file, an email will be sent to the birthday person with a personalized message.

## Code Explanation

- The script reads the current date and checks if it matches any birthday in the `birthdays.csv` file.
- If a match is found, it selects a random birthday message template from the `letter_templates` directory.
- The script replaces the `[NAME]` placeholder in the template with the birthday person's name.
- It then sends an email using the SMTP protocol with the personalized message.

## License

This project is licensed under the MIT License.
