import requests
from bs4 import BeautifulSoup

host = "https://lendrive.web.id"

def getOngoing(page=1):
    ret = []
    data = BeautifulSoup(requests.get(
        host + f"/page/{page}/").text, features="html.parser")
    for anime in data.select('div.bixbox.bbnofrm > div.releases.latesthome + div.listupd.normal div.bsx'):
        aElement = anime.find('a')
        url = aElement.attrs['href']
        title = aElement.attrs['title']
        img = anime.find('img').attrs['src']
        eps = anime.find('span', {'class': 'epx'}).text
        ret.append({'title': title, 'url': url, 'eps': eps, 'img': img})
    return ret