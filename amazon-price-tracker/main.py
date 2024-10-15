from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from notification_manager import NotificationManager

load_dotenv()

# product_url = "https://appbrewery.github.io/instant_pot/"

product_url = "https://www.amazon.de/-/en/ASICS-Womens-Running-Shoes-Yellow/dp/B0D8FJM8M5/ref=sr_1_4?crid=30IFVHLHF7Z4X&dib=eyJ2IjoiMSJ9.C5eP8a4zychjF481AiOVgSX2cktWhtivPbNzLm5Jd3YPdJ-chBtx7jmiwySa0o9qDRNmmxmIOznxP-gKDvG9tdW3IR9jVlIIJ8oJLneuoSFV3_5fwOaJLdB4RJxWmzaIIRr_7X5xiv9ltb9yaREybAL8KSgX_alvRoeA3ilhomUNGS07mwG-DfZpMY9TcW8lUHdvyXuRMrWWhqHxL57_WSxMmffbpSDXh4JnnvaZnUo50e8Xso6DRrffxA0iWLHduVuFuX5sUtnUc9JpQnzhMFYoEzJvhZ0DMePoQnqIhV0.xqLsjk1SgqK28RO69lFZH7nU_j7k6SABjULulnXqh08&dib_tag=se&keywords=asics%2Bnovablast%2B4&qid=1727897561&sprefix=asics%2Bnovablast%2B4%2Caps%2C90&sr=8-4&th=1"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ru-RU,ru;q=0.9,uk-UA;q=0.8,uk;q=0.7,en-US;q=0.6,en;q=0.5,lt;q=0.4",
    "Sec-Ch-Ua": "\"Not_A Brand\";v=\"99\", \"Google Chrome\";v=\"109\", \"Chromium\";v=\"109\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}
response = requests.get(url=product_url, headers=headers)
page = response.text

soup = BeautifulSoup(page, "html.parser")
print(soup.prettify())
# price = float(soup.find(name="span", class_="aok-offscreen").getText().split("$")[1])
price = float(soup.find(name="span", class_="a-offscreen").getText().split("€")[1])
product_title = soup.find(name="span", id="productTitle").getText()
print(price)

notification_manager = NotificationManager()

if price < 200:
    message = f"Subject: Amazon Price Alert!\n\n{product_title} is now {price}\n {product_url}".encode('utf-8')
    print(message)
    notification_manager.send_email(message)
