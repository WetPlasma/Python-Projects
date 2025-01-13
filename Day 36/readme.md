# Stock and News Alert

This script fetches the latest stock prices for a specified company and sends an email alert if there is a significant change in the stock price. It also fetches the latest news articles related to the company and includes them in the email.

## Requirements

- Python 3.x
- `requests` library
- `smtplib` library

## Installation

1. Clone the repository or download the `main.py` file.
2. Install the required Python libraries using pip:
    ```sh
    pip install requests
    ```

## Configuration

1. Set up your email credentials and API keys in the `main.py` file:
    ```python
    my_email = "your_email@gmail.com"
    password = "your_email_password"

    STOCK_NAME = "TSLA"
    COMPANY_NAME = "Tesla Inc"

    STOCK_ENDPOINT = "https://www.alphavantage.co/query"
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    api_key = "your_alpha_vantage_api_key"
    news_api_key = "your_news_api_key"
    ```

2. Ensure that "Less secure app access" is enabled for your Gmail account if you are using Gmail.

## Usage

Run the script using Python:
```sh
python main.py
