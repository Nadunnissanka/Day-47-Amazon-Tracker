from bs4 import BeautifulSoup
import requests
import lxml
import smtplib

MY_EMAIL = "nadunnissankatest@gmail.com"
MY_PASSWORD = "nadun123"
RECIVE_MAIL = "nadunnissanka@yahoo.com"

WEBSITE_URL = "https://www.daraz.lk/products/jbl-charge-3-mini-bluetooth-speaker-i104913336-s1011918888.html?spm=a2a0e.home.flashSale.7.675a4625T4F5Il&search=1&mp=1&c=fs"
header = {
    "Accept-Language": "en-US,en;q=0.9",
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Cookie': 'PHPSESSID=65lphdbedvscjnfh99tsjpdni7; _ga=GA1.2.703285383.1628172687; _gid=GA1.2.1002561115.1628172687',
    'Upgrade-Insecure-Requests': '1',
    'X-Http-Proto': 'HTTP/1.1',
    'X-Real-Ip': '124.43.35.65',
    'Accept-Encoding': 'gzip, deflate',
}
response = requests.get(url=WEBSITE_URL, headers=header)
webpage = response.text
print(webpage)

soup = BeautifulSoup(webpage, "lxml")

heading = soup.find(name="span", class_="pdp-price_type_normal").getText()
# heading = "Rs.1100"
current_price = int(heading.split(".")[1])

if current_price < 1250:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECIVE_MAIL,
            msg=f"Subject:Price Drop Alert\n\nitem price is under Rs.1250\nLink: {WEBSITE_URL}"
        )
