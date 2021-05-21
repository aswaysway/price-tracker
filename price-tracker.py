import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.com/Logitech-Lightspeed-Rechargeable-Compatible-Ambidextrous/dp/B07NSVMT22/ref=sr_1_1_sspa?dchild=1&keywords=G903&qid=1606032845&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMFU0N0VENE1LWU1BJmVuY3J5cHRlZElkPUEwNjI0MDY5MlZLWEY1RkhOTFpVNSZlbmNyeXB0ZWRBZElkPUEwNTg5OTAxSVhFMUsySzVWQkNQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}

mail_username = 'username@gmail.com'
mail_password = 'Generated app password'

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="prodcutTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(mail_username, mail_password)
    
    subject = 'PRICE FELL DOWN!'
    body = 'Check the Amazon link: https://www.amazon.com/Logitech-Lightspeed-Rechargeable-Compatible-Ambidextrous/dp/B07NSVMT22/ref=sr_1_1_sspa?dchild=1&keywords=G903&qid=1606032845&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzMFU0N0VENE1LWU1BJmVuY3J5cHRlZElkPUEwNjI0MDY5MlZLWEY1RkhOTFpVNSZlbmNyeXB0ZWRBZElkPUEwNTg5OTAxSVhFMUsySzVWQkNQJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        mail_username,
        mail_password,
        msg
    )
    
    print('EMAIL HAS BEEN SUCCESSFULLY SENT!')

    server.quit()

while(True):
    check_price()
    time.sleep(60*60*24)
