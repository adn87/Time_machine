from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"

music_year = input("which year do you want to travel to? type the data in this format YYYY-MM-DD:")

response = requests.get(URL + music_year)
music_webpage = response.text
soup = BeautifulSoup(music_webpage, "html.parser")

song_names = soup.select("li ul li h3")
songs_list = [song.getText().strip() for song in song_names]

with open("songs.txt", mode="w", encoding="utf8") as file:
    [file.write(f"{name}\n") for name in songs_list]