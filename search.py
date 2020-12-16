
from googlesearch import search
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen

def title_extractor(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html,'html.parser')
    for title in soup.find_all("title"):
        a = (title.get_text())
        return a




def build_container(query):
    result = search(query,stop=10)
    l = []
    d = {}
    for i in result:
        d["url"]=i
        d["Title"]=title_extractor(i)
        l.append(d)
    return l

def urls(query):
    result = search(query,stop=15)
    return result

print(build_container("books"))

