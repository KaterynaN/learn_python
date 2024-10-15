import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print 3 main news about
# company and send in messages via wattsUp.

api_key = os.environ.get('ALPHA_VANTAGE_API_KEY')
news_api_key = os.environ.get('NEWS_API_KEY')
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')


def get_news():
    news_params = {
        "q": COMPANY_NAME,
        "searchIn": "title",
        "apiKey": news_api_key,
        "sortBy": "publishedAt",
        "pageSize": 3
    }

    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"]
    news = [{'headline': item['title'], 'description': item['description']} for item in news_data]
    return news


def send_news_to_wattsup(news_data, arrow, percent):
    client = Client(account_sid, auth_token)
    send_from = os.environ.get('FROM_TWILIO_WHATSAPP_NUMBER')
    send_to = os.environ.get('TO_TWILIO_WHATSAPP_NUMBER')
    for item in news_data:
        message_body = f'{STOCK_NAME}: {arrow}{percent}%\n Headline: {item['headline']}\n Brief: {item['description']}'

        message = client.messages.create(
            from_=send_from,
            body=message_body,
            to=send_to,
        )
        print(message.status)
        print(message_body)


stock_params = {
    "function": 'TIME_SERIES_DAILY',
    "symbol": STOCK_NAME,
    "apikey": api_key
}
response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday = data_list[0]
yesterday_stock_closing_price = yesterday["4. close"]
before_yesterday = data_list[1]
before_yesterday_stock_closing_price = before_yesterday["4. close"]

print(f"Yesterday:{yesterday_stock_closing_price}, Before_yesterday:{before_yesterday_stock_closing_price}")

difference = (float(yesterday_stock_closing_price) - float(before_yesterday_stock_closing_price))
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / float(yesterday_stock_closing_price)) * 100)
if abs(diff_percent) > 2:
    news = get_news()
    send_news_to_wattsup(news_data=news, arrow=up_down, percent=diff_percent)
