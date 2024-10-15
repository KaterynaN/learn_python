from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfInbYmC5-1L0UvTJSr6dL0UesUIGxHcX4AifYtroF4CPAYbw/viewform?usp=sf_link"


load_dotenv()

url = "https://appbrewery.github.io/Zillow-Clone/"

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
response = requests.get(url=url, headers=headers)
page = response.text

soup = BeautifulSoup(page, "html.parser")
links_list = []
links = soup.find_all(name='a', class_="property-card-link")
for link in links:
    links_list.append(link['href'])
print(len(links_list))

price_list = []
prices = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
for price in prices:
    price_list.append(price.getText().strip('+/mo bd').replace('+ 1', ''))
print(len(price_list))

address_list = []
addresses = soup.find_all(name='address')
for address in addresses:
    address_list.append(address.getText().strip())
print(len(address_list))


for i in range(len(links_list)):
    driver.get(form_url)
    time.sleep(2)
    form_address = driver.find_element(By.XPATH, '//input[@type="text"]')
    form_address.send_keys(address_list[i])
    form_price = driver.find_element(By.XPATH, '(//input[@type="text"])[2]')
    form_price.send_keys(price_list[i])
    form_link = driver.find_element(By.XPATH, '(//input[@type="text"])[3]')
    form_link.send_keys(links_list[i])
    submit_button = driver.find_element(By.CSS_SELECTOR, "div[role='button'][aria-label='Submit']")
    submit_button.click()

