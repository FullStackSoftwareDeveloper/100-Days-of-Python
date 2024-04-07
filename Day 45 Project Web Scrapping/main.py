from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
movies = response.text

soup = BeautifulSoup(movies, "html.parser")

movie_list = soup.find_all(name="h3", class_="title")

titles = [movie.getText() for movie in movie_list]

titles.reverse()

print(titles)