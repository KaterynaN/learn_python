import requests
from bs4 import BeautifulSoup
import re

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies]
movie_list = movie_titles[::-1]
movies_cleaned = [re.split('[):]', movie.getText())[-1] for movie in movies]
print(movie_list)

for movie in movie_list:
    with open("movie_list.txt", 'a') as file:
        file.write(f"{movie}\n")
