from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

load_dotenv()
date = input("What year you would like to travel to? Write in YYY-MM-DD format")
# date = "2000-08-12"
year = date.split("-")[0]
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
playlist = response.text

soup = BeautifulSoup(playlist, "html.parser")
song_titles = [song.getText().strip("\n\t") for song in
               soup.find_all(name="h3", id="title-of-a-story", class_="a-no-trucate")]
print(song_titles)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
                                               client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
                                               redirect_uri=os.environ.get("SPOTIFY_APP_REDIRECT_URI"),
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path="token.txt",
                                               username="SPOTIFY_USER_NAME"))
user_id = sp.current_user()["id"]

song_uris = []
for title in song_titles:
    result = sp.search(q=f'track:{title} year:{2000}', type='track')
    # pprint.pp(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")

play_list = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=play_list['id'], items=song_uris)


