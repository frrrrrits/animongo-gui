import requests
from bs4 import BeautifulSoup

host = "https://lendrive.web.id"

# still confused and learn for this error handling
def get_ongoing(page=1):
    try:
        r = requests.get(host + f"/page/{page}/")
        r.raise_for_status()
        arr = []
        data = BeautifulSoup(r.text, features="html.parser")
        for anime in data.select('div.bixbox.bbnofrm > div.releases.latesthome + div.listupd.normal div.bsx'):
            aElement = anime.find('a')
            url = aElement.attrs['href']
            title = aElement.attrs['title']
            img = anime.find('img').attrs['src']
            eps = anime.find('span', {'class': 'epx'}).text
            arr.append({'title': title, 'url': url, 'eps': eps, 'img': img})
        return arr
    except requests.exceptions.RequestException as e:
        return e

def get_search(query):
    data = BeautifulSoup(requests.get(host+"/?s={}".format(query)).text, features="html.parser")
    print(data)