import requests
import smtplib
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Mivi-Saxo-Wireless-Bluetooth-Earphones/dp/B075XLGW8J/ref=sr_1_2?keywords=mivi+saxo&qid=1572534819&sr=8-2'



def send_mail():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

   

     subject = 'PRICE FELL DOWN'
     body = 'Check this Link   https://www.amazon.in/Mivi-Saxo-Wireless-Bluetooth-Earphones/dp/B075XLGW8J/ref=sr_1_2?keywords=mivi+saxo&qid=1572534819&sr=8-2'

     msg = f"Subject: {subject}\n\n{body}"

     server.sendmail(
         '',
         '',
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
