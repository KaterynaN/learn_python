from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.select(selector=".titleline a")
article_texts = []
article_links = []
for article in articles:
    article_tag = article.getText()
    article_texts.append(article_tag)
    article_link = article.get("href")
    article_links.append(article_link)
article_scores = [int(score.getText().split()[0]) for score in soup.select(selector=".score")]

index = article_scores.index(max(article_scores))

print(f"{article_texts[index]} \n{article_links[index]} \n{article_scores[index]}")



# with open("website.html") as file:
#     data = file.read()
#
# soup = BeautifulSoup(data, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# anchor_tags = soup.find_all(name="a")
#
# for tag in anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name='h3', class_="heading")
# print(section_heading)