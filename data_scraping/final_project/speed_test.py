import requests
import time

from multiprocessing import Pool

HEADERS = {
    'Accept-Language': 'en',
    'X-FORWARDED-FOR': '2.21.184.0'
}

urls = [
    'https://www.imdb.com/title/tt21137852/fullcredits/',
    'https://www.imdb.com/title/tt0762125/fullcredits/',
    'https://www.imdb.com/title/tt7975244/fullcredits/',
    'https://www.imdb.com/title/tt2126355/fullcredits/',
    'https://www.imdb.com/title/tt4630562/fullcredits/',
    'https://www.imdb.com/title/tt1397514/fullcredits/',
    'https://www.imdb.com/title/tt0870154/fullcredits/',
    'https://www.imdb.com/title/tt0421206/fullcredits/',
    'https://www.imdb.com/title/tt6806448/fullcredits/',
    'https://www.imdb.com/title/tt0499554/fullcredits/',
    'https://www.imdb.com/title/tt2283362/fullcredits/',
    'https://www.imdb.com/title/tt1469304/fullcredits/',
    'https://www.imdb.com/title/tt3521164/fullcredits/',
    'https://www.imdb.com/title/tt1596343/fullcredits/',
    'https://www.imdb.com/title/tt0425061/fullcredits/',
    'https://www.imdb.com/title/tt0419706/fullcredits/',
    'https://www.imdb.com/title/tt0808510/fullcredits/',
    'https://www.imdb.com/title/tt7991608/fullcredits/',
    'https://www.imdb.com/title/tt1386588/fullcredits/',
    'https://www.imdb.com/title/tt0277296/fullcredits/',
    'https://www.imdb.com/title/tt2820852/fullcredits/',
    'https://www.imdb.com/title/tt8912936/fullcredits/',
    'https://www.imdb.com/title/tt5758778/fullcredits/',
    'https://www.imdb.com/title/tt1391137/fullcredits/',
    'https://www.imdb.com/title/tt1905041/fullcredits/',
    'https://www.imdb.com/title/tt1414382/fullcredits/',
    'https://www.imdb.com/title/tt1433108/fullcredits/',
    'https://www.imdb.com/title/tt1980209/fullcredits/',
    'https://www.imdb.com/title/tt3614530/fullcredits/',
    'https://www.imdb.com/title/tt0351977/fullcredits/',
    'https://www.imdb.com/title/tt0201694/fullcredits/',
    'https://www.imdb.com/title/tt1583421/fullcredits/',
    'https://www.imdb.com/title/tt0377471/fullcredits/',
    'https://www.imdb.com/title/tt1267297/fullcredits/',
    'https://www.imdb.com/title/tt0882977/fullcredits/',
    'https://www.imdb.com/title/tt1489889/fullcredits/',
    'https://www.imdb.com/title/tt2171867/fullcredits/',
    'https://www.imdb.com/title/tt0209163/fullcredits/',
    'https://www.imdb.com/title/tt6513120/fullcredits/',
    'https://www.imdb.com/title/tt6264654/fullcredits/',
    'https://www.imdb.com/title/tt0405336/fullcredits/',
    'https://www.imdb.com/title/tt0327850/fullcredits/',
    'https://www.imdb.com/title/tt14344936/fullcredits/',
    'https://www.imdb.com/title/tt1075417/fullcredits/',
    'https://www.imdb.com/title/tt0492956/fullcredits/',
    'https://www.imdb.com/title/tt2231461/fullcredits/',
]


start = time.time()
with Pool(13) as p:
    print(p.map(requests.get, urls))

end = time.time()
print('time elapsed', end - start, 'secs')
