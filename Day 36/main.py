import requests
import smtplib

my_email = "mail"
password = "pass"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

api_key = "key"
news_api_key = "key"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

difference = yesterday_closing_price - day_before_yesterday_closing_price
diff_percentage = (difference / day_before_yesterday_closing_price) * 100

if abs(diff_percentage) > 0.0001:
    print(abs(diff_percentage))
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_article = [
        f"Headline: {article['title']}. \nBrief: {article['description']}"
        for article in three_articles
    ]

    message = f"Subject:TSLA: 🔺{diff_percentage}%\n\n {formatted_article[0]}\n{formatted_article[1]}\n{formatted_article[2]}"
    message = message.encode("utf-8")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="moonknigh7200@gmail.com",
                msg=message,
            )
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
