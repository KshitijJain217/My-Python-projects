import requests
from bs4 import BeautifulSoup
import smtplib

headers = {'Accept-Language': "en-US,en;q=0.9",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                         "(KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"}

# amazon_static = "https://appbrewery.github.io/instant_pot/"
amazon_live = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(amazon_live, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

price_whole = soup.find(name="span", class_="a-price-whole").get_text()
price_fraction = soup.find(name="span", class_="a-price-fraction").get_text()
price = float(price_whole + price_fraction)
# print(price)

title = soup.find(id="productTitle").get_text().strip()
# print(title)

BUY_PRICE = 150

if price < BUY_PRICE:
    message = f"{title} is on sale for {price}!"
    # print(message)

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )


