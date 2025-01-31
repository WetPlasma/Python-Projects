# Price Tracker Script

This Python script tracks the price of a product from an e-commerce website and sends an email notification when the price drops below a specified amount.

## Requirements

Ensure you have the following installed:
- Python 3.x
- Required libraries:
  - `beautifulsoup4`
  - `requests`
  - `smtplib` (built-in)

Install dependencies using:
```sh
pip install beautifulsoup4 requests
```

## Configuration

1. **Set Product URL:** Replace `'PRODUCT URL'` with the actual product link.
2. **Set Headers:** Replace `'YOUR USER AGENT'` and `'YOUR ACCEPT'` with appropriate values. You can find your User-Agent by searching "What is my User-Agent?" in a browser.
3. **Set Email Credentials:** Replace `'YOUR MAIL ADDRESS'`, `'YOUR APP PASSWORD'`, `'SENDERS MAIL'`, and `'RECIVER'S MAIL'` with appropriate email credentials.

## Usage

Run the script using:
```sh
python script.py
```

If the price drops below 400, an email alert will be sent.

## Note

- Some e-commerce websites may block web scraping. Ensure compliance with the site's terms of service.
- Consider using `time.sleep()` to delay requests and avoid getting blocked.
- Use an App Password if using Gmail for authentication instead of the actual password.

## License

This project is for educational purposes only. Use responsibly!

