import bs4
import requests
import smtplib

link = 'PRODUCT URL'
header = {
    'User-Agent': 'YOUR USER AGENT',
    'Accept': 'YOUR ACCEPT',
}

response = requests.get(link, headers=header)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
price = soup.find('span', class_='a-offscreen')
price = price.text
price = price.replace('₹', '').replace(',', '').strip()

price = int(float(price))
if price < 400:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user='YOUR MAIL ADDRESS', password='YOUR APP PASSWORD')
        connection.sendmail(from_addr='SENDERS MAIL', to_addrs='RECIVER,S MAIL',
                            msg=f"Subject:BUY NOW!\n\n "
                                f"best pricedetected {price} buy now!")
