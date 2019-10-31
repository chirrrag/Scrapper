import requests
import smtplib
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Mivi-Saxo-Wireless-Bluetooth-Earphones/dp/B075XLGW8J/ref=sr_1_2?keywords=mivi+saxo&qid=1572534819&sr=8-2'

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0"}

def send_mail():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('mailstochiragsapra@gmail.com', 'jxotmeznuejmtahf')

     subject = 'PRICE FELL DOWN'
     body = 'Check this Link   https://www.amazon.in/Mivi-Saxo-Wireless-Bluetooth-Earphones/dp/B075XLGW8J/ref=sr_1_2?keywords=mivi+saxo&qid=1572534819&sr=8-2'

     msg = f"Subject: {subject}\n\n{body}"

     server.sendmail(
         'mailstochirag@gmail.com',
         'csapra121@gmail.com',
         msg
     )
     print("HEY EMAIL HAS BEEN SENT")

     server.quit()


def check_price():

    page = requests.get(url, headers = headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.prettify())

    title = soup.find(id = "productTitle").get_text()
    print(title.strip())

    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[1:7]
    converted_price = float(converted_price.replace(',',''))
    print(converted_price)

    if converted_price < 5000:
        send_mail()


check_price()