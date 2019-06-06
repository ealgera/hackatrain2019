"""
Just like scrap-02 but now with a file instead of going to the Internet

Python program to scrape info about trending repositories from https://github.com/trending
Scrape: auyhor, projectname, stars and url from the site
Sort all on Stars
Create a CSV file with the scraped data
Import the data into Pandas
And create a Bar-graph
"""

from bs4 import BeautifulSoup
import requests

import csv

import pandas as pd
import matplotlib.pyplot as plt

url = "https://github.com/trending"
my_file = r"../Trending repositories on GitHub today.html"

soup = BeautifulSoup(open(my_file), "html.parser")
#print(soup.prettify)

repo_list = soup.find("ol", {"class": "repo-list"})

repo_trends = []
for repo_element in repo_list.find_all("li", {"class": "col-12 d-block width-full py-4 border-bottom"}):
    repo_author, repo_name = repo_element.find("a").text.split(" / ")
    repo_stars = repo_element.find("a", {"class": "muted-link d-inline-block mr-3"})

    repo_link = "https://github.com" + repo_element.find("a").get("href")

    repo_trends.append([repo_author.strip(), repo_name.strip(), int(repo_stars.text.strip().replace(",","")), repo_link])

repo_trends = sorted(repo_trends, key=lambda x: x[2], reverse=True)
#
for elem in repo_trends:
    print(elem)
#
## Save list to CSV file
#with open("trends.csv","w") as csv_file:
#    wr = csv.writer(csv_file)
#    wr.writerows(repo_trends)
#
#df = pd.read_csv("trends.csv", names=["Author", "Name", "Stars", "Link"])
#
#df.set_index("Author", inplace=True)
#print(df)
#
#p = df.Stars.plot(kind="bar")
#plt.show()