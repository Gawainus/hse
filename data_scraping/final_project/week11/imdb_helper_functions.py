import requests
import time
import os

from multiprocessing import Pool
from bs4 import BeautifulSoup

POOL_SIZE = 13
DISK_CACHE_DIR = 'cache'

SITE_URL = 'https://www.imdb.com'
HEADERS = {
    'Accept-Language': 'en',
    'X-FORWARDED-FOR': '2.21.184.0'
}

MOVIE_FILTERS = ['(announced)', '(pre-production)', '(post-production)', '(completed)',
                 '(TV Series)', '(TV Special)', '(TV Mini Series)', '(TV Movie)', '(TV Series short)',
                 '(TV Mini Series short)', '(TV Series documentary)', '(TV Series documentary short)',
                 '(TV Mini Series documentary)',
                 '(Music Video short)',
                 '(voice)',
                 '(Video short)', '(Video)', '(Video Game)', '(Short)']


def get_checkpoint_name_from_url(url):
    fname = '_'.join(url.split('/')[-3: -1])
    return fname


def get_url_from_fname(fname):
    return '/' + '/'.join(fname.split('.')[0].split('_')) + '/'


def save_parsed(url, urls):
    """

    :param url:
    :param urls:
    :return:
    """
    # make sure cache_bak dir exists.
    cache_dir = os.path.join(os.getcwd(), DISK_CACHE_DIR)
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)

    fname = get_checkpoint_name_from_url(url)
    with open(f'./{DISK_CACHE_DIR}/{fname}.txt', 'w') as f:
        for u in urls:
            f.writelines(u + '\n')


def get_p(x):
    while True:
        try:
            return requests.get(x, HEADERS)
        except requests.exceptions.ConnectionError:
            time.sleep(3)


def get_set_from_list(pair_list):
    return set([url for _, url in pair_list])


def _get_actors_by_movie_soup(cast_page_soup, num_of_actors_limit=None):
    tb = cast_page_soup.find('table', {'class': 'cast_list'})
    actors = tb.find_all('tr', {'class': ['odd', 'even']})
    name_to_link = {}
    for i, a in enumerate(actors):
        if num_of_actors_limit and i >= num_of_actors_limit:
            break

        info = a.find_all('a')[1]
        actor_name = info.text.strip()
        link = info['href']
        name_to_link[actor_name] = link

    return [(k, v) for k, v in name_to_link.items()]


def _get_movies_by_actor_soup(actor_page_soup, num_of_movies_limit=None):
    node = actor_page_soup.find('div', id=['filmo-head-actor', 'filmo-head-actress'])
    if not node:
        return []

    tb = node.findNext('div')
    filmos = tb.find_all('div', {'class': ['filmo-row odd', 'filmo-row even']})
    name_to_link = {}
    counter = 0
    for f in filmos:
        if num_of_movies_limit and counter >= num_of_movies_limit:
            break

        info = f.find_all('a')
        if any(x in f.text for x in MOVIE_FILTERS):
            continue

        title = info[0]
        name = title.text
        link = title['href']
        name_to_link[name] = link
        counter += 1

    return [(k, v) for k, v in name_to_link.items()]


def split_list(arr, n):
    return [arr[i:i + n] for i in range(0, len(arr), n)]


class Cache:
    """
    """
    def __init__(self, type, suffix=''):
        self.type = type
        self.suffix = suffix
        self.storage = {}

        # try to recover from disk
        cache_dir = os.path.join(os.getcwd(), DISK_CACHE_DIR)
        if os.path.exists(cache_dir):
            folder = f'./{DISK_CACHE_DIR}'
            files = os.listdir(folder)
            files = [f for f in files if self.type in f and f.endswith('.txt')]
            keys = [get_url_from_fname(os.path.splitext(fname)[0]) for fname in files]
            for k, fname in zip(keys, files):
                with open(f'{folder}/{fname}', 'r') as f:
                    lns = f.readlines()
                    if k not in self.storage:
                        self.storage[k] = set()

                    for line in lns:
                        line = line.strip()
                        self.storage[k].add(line)

            print('Recovered', len(self.storage.keys()), self.type, 'urls from disk.')

    def get_pages(self, urls, limit):
        # print(self.storage)
        print(f'Requesting {len(urls)} urls from {self.type} cache')
        missed_urls = [url for url in urls if url not in self.storage]
        if len(missed_urls) > 0:
            print(f'Getting {len(missed_urls)} urls through http requests')

            # make sure cache_bak dir exists.
            cache_dir = os.path.join(os.getcwd(), DISK_CACHE_DIR)
            if not os.path.exists(cache_dir):
                os.mkdir(cache_dir)

            with Pool(POOL_SIZE) as p:
                finished_count = 0
                for small_urls_list in split_list(missed_urls, POOL_SIZE * 7):
                    full_urls = [SITE_URL + mu + self.suffix for mu in small_urls_list]

                    start = time.time()
                    pages = p.map(get_p, full_urls)
                    end = time.time()

                    for i, page in enumerate(pages):
                        if page.status_code != 200:
                            print('skipping:', full_urls[ i])
                            continue

                        bs = BeautifulSoup(page.text, features="html.parser")
                        print(full_urls[i])
                        if self.type == 'title':
                            mapped_urls = _get_actors_by_movie_soup(bs, limit)
                        else:
                            mapped_urls = _get_movies_by_actor_soup(bs, limit)

                        mapped_urls = [u for _, u in mapped_urls]
                        save_parsed(small_urls_list[i], mapped_urls)
                        self.storage[small_urls_list[i]] = set(mapped_urls)

                    finished_count += len(small_urls_list)
                    print('time elapsed', end - start, 'secs for batch of',
                        len(small_urls_list), ',', len(missed_urls) - finished_count, 'left')

        ret_set = set()
        for url in urls:
            ret_set = ret_set.union(self.storage[url])

        return list(ret_set)


