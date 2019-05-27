"""
Python program to get scrape info about trending repositories from https://econpy.pythonanywhere.com/ex/XXX.html
"""

from bs4 import BeautifulSoup
import requests

url = "https://github.com/trending"

response = requests.get(url)
#print(response)

my_html = response.text
soup = BeautifulSoup(my_html, 'html.parser')
#print(soup.prettify)

repo_list = soup.find("ol", {"class": "repo-list"})
#print(repo_list)
repo_element = repo_list.find("li", {"class": "col-12 d-block width-full py-4 border-bottom"})
#print(repo_element)

#repo_author = repo_element.find("a")
#print(repo_author.text)

#repo_author, repo_name = repo_element.find("a").text.split(" / ")
#print(repo_author, repo_name)

repo_trends = []
for repo_element in repo_list.find_all("li", {"class": "col-12 d-block width-full py-4 border-bottom"}):
    repo_author, repo_name = repo_element.find("a").text.split(" / ")
    repo_stars = repo_element.find("a", {"class": "muted-link d-inline-block mr-3"})
    #print(repo_author.strip(), repo_name.strip(), repo_stars.text.strip())

    repo_link = "https://github.com" + repo_element.find("a").get("href")

    repo_trends.append([repo_author.strip(), repo_name.strip(), int(repo_stars.text.strip().replace(",","")), repo_link])

repo_trends = sorted(repo_trends, key=lambda x: x[2], reverse=True)

for elem in repo_trends:
    print(elem)
