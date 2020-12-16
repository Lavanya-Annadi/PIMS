# import google
from googlesearch import search
from bs4 import BeautifulSoup
import requests
def title_extractor(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    for title in soup.find_all("title"):
        a = (title.get_text())
        return a
def build_container(query):
    result = search(query, stop=10)
    l = []

    for i in result:
        d = {}
        d["url"] = i
        d["title"] = title_extractor(i)
        l.append(d)
    return l


