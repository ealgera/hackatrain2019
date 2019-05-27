"""
Python program to get buyer en price info from all pages of: http://econpy.pythonanywhere.com/ex/XXX.html
"""

from bs4 import BeautifulSoup
import requests
import csv

url = "http://econpy.pythonanywhere.com/ex/001.html"

response = requests.get(url)
#print(response)

my_html = response.text
#print(my_html)

soup = BeautifulSoup(my_html, 'html.parser')
#print(soup.prettify)

pages = soup.find("div")
#print(pages)

ahref = pages.find("a")
#print(ahref.get("href"))

ahrefs = pages.find_all("a")
#for a in ahrefs:
#    print(a.get("href"))

page_list = [a.get("href") for a in ahrefs]
page_list.insert(0, url)
#print(page_list)

#buyer_info = soup.find("div", title="buyer-info")
#print(buyer_info)

#buyer_name  = buyer_info.find("div", title="buyer-name")
#buyer_price = buyer_info.find("span")
#print(buyer_name.text)
#print(buyer_price.text)

#buyer_info = soup.find_all("div", title="buyer-info")
#print(buyer_info)

#buyers = []
#for buyer in soup.find_all("div", title="buyer-info"):
#    #print(buyer)
#    buyer_name  = buyer.find("div", title="buyer-name")
#    buyer_price = buyer.find("span")
#    #print(buyer_name.text, buyer_price.text)
#    buyers.append([buyer_name.text, buyer_price.text])

#print(buyers)

def get_info(bs_soup):
    buyers = []
    for buyer in soup.find_all("div", title="buyer-info"):
        buyer_name  = buyer.find("div", title="buyer-name")
        buyer_price = buyer.find("span")
        buyers.append([buyer_name.text, buyer_price.text])
    return buyers

all_buyers = []
for url in page_list:
    print(f"Parsing... [{url}]")
    response = requests.get(url)
    my_html = response.text
    soup = BeautifulSoup(my_html, 'html.parser')
    all_buyers += get_info(soup)

#print(all_buyers)

with open('buyers.csv', 'w') as writeCSV:
    writer = csv.writer(writeCSV, delimiter=",", quotechar = '"', quoting=csv.QUOTE_ALL)
    writer.writerow(["Buyer", "Price"])
    writer.writerows(all_buyers)
