from bs4 import BeautifulSoup
import lxml
import requests

response=requests.get(url="https://www.empireonline.com/movies/features/best-movies-2/")
content= response.text
soup=BeautifulSoup(content, "html.parser")
print(soup.prettify())
movies_names=soup.select(".listicleItem_listicle-item__title__hW_Kn")
for i in range(len(movies_names)-1, -1, -1):
    movie=movies_names[i].getText()
    print(movie)
    with open("movies.txt", mode="a") as file:
        file.write(f"{movie}\n")