from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
movies_page = response.text

soup = BeautifulSoup(movies_page, "html.parser")

movie_names = soup.find_all(name="h3", class_="jsx-4245974604")
# print(movie_names)


movie_list = []
for article_tag in movie_names:
    text = article_tag.getText()
    movie_list.append(text)
print(movie_list[::-1])

for index in movie_list[-1::-1]:
    print(index)
    with open("top-100-movie-list.txt", "a") as document:
        document.write(f"{index}\n")

