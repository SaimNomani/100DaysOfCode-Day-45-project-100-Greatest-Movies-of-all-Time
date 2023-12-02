from bs4 import BeautifulSoup
import lxml
import requests

# # with open("website.html", encoding="utf-8") as file:
# #     contents=file.read()

# # soup=BeautifulSoup(contents, "html.parser")
# # print(soup.a)
# # print(soup.prettify())

# # a_tgs=soup.find_all(name="a")
# # print(a_tgs)
# # for tag in a_tgs:
# #     print(tag.getText())
# #     print(tag.get("href"))
# # headings=soup.find(name="h1", id="name")
# # print(headings.get_text())
# # section_headings=soup.find(name="h3", class_="heading")
# # print(section_headings)

# # name=soup.select_one("#name")
# # print(name)

# # headings=soup.select(".heading")
# # print(headings)

# response=requests.get(url="https://news.ycombinator.com/news")
# print(response.status_code)
# soup=BeautifulSoup(response.text, "html.parser")
# print(soup.title)
# title_lines=soup.select(".titleline a")
# print(title_lines)
# for line in title_lines:
#     print(line.get_text())
# print(len(title_lines))

# for line in title_lines:
#     print(line.get("href"))

# scores=soup.select(".score")
# for score in scores:
#     print(score.getText())