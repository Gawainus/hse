import time
import imdb_helper_functions as hf

from multiprocessing import Pool


def get_actors_by_movie_soup(cast_page_soup, num_of_actors_limit=None):
    return hf._get_actors_by_movie_soup(cast_page_soup, num_of_actors_limit)


def get_movies_by_actor_soup(actor_page_soup, num_of_movies_limit=None):
    return hf._get_movies_by_actor_soup(actor_page_soup, num_of_movies_limit)


def get_movie_distance(actor_start_url,
                       actor_end_url,
                       num_of_actors_limit=None,
                       num_of_movies_limit=None):
    actor_end_page = requests.get(actor_end_url, headers=hf.HEADERS)
    actor_end_bs = BeautifulSoup(actor_end_page.text, features="html.parser")
    movie_end_list = get_movies_by_actor_soup(actor_end_bs, num_of_movies_limit)
    target_set = hf.get_set_from_list(movie_end_list)

    movie_cache = hf.Cache('title', 'fullcredits/')
    actor_cache = hf.Cache('name')

    distance = 1
    dk_actors = ['/' + actor_start_url.strip(hf.SITE_URL) + '/']

    for k in range(0, 10):
        print('K:', k)

        dk_movies = actor_cache.get_pages(dk_actors, num_of_movies_limit)
        inter = set(dk_movies).intersection(target_set)
        if len(inter) > 0:
            print('inter', inter)
            break

        dk_actors = movie_cache.get_pages(dk_movies, num_of_movies_limit)
        distance += 1

    return distance


def get_movie_descriptions_by_actor_soup(actor_page_soup):
    movies = get_movies_by_actor_soup(actor_page_soup)

    def get_desc(res):
        bs = BeautifulSoup(res.text, features="html.parser")
        return bs.find('span', attrs={'data-testid': 'plot-xl', 'class': 'sc-16ede01-2 gXUyNh'}).text

    full_urls = [hf.SITE_URL + url for _, url in movies]
    with Pool(hf.POOL_SIZE) as p:
        start = time.time()
        pages = p.map(hf.get_p, full_urls)
        end = time.time()
        print('time elapsed', end - start, 'secs')

    descriptions = [get_desc(p) for p in pages]

    return descriptions


if __name__ == '__main__':
    import requests
    from bs4 import BeautifulSoup

    # title_page = requests.get('https://www.imdb.com/title/tt2382320/fullcredits/', headers=hf.HEADERS)
    # title_page_bs = BeautifulSoup(title_page.text, features="html.parser")
    # print(get_actors_by_movie_soup(title_page_bs, 1))
    # print(get_actors_by_movie_soup(title_page_bs, 3))
    # print(get_actors_by_movie_soup(title_page_bs))
    #
    # actor_page = requests.get('https://www.imdb.com/name/nm0185819/', headers=hf.HEADERS)
    # actor_page_soup = BeautifulSoup(actor_page.text, features="html.parser")
    # print(get_movies_by_actor_soup(actor_page_soup, 1))
    # print(get_movies_by_actor_soup(actor_page_soup, 3))
    # print(get_movies_by_actor_soup(actor_page_soup))
    #
    # actress_page = requests.get('https://www.imdb.com/name/nm2244205', headers=hf.HEADERS)
    # actress_page_soup = BeautifulSoup(actress_page.text, features="html.parser")
    # print(get_movies_by_actor_soup(actress_page_soup, 1))
    # print(get_movies_by_actor_soup(actress_page_soup, 3))
    # print(get_movies_by_actor_soup(actress_page_soup))


    dwayne_johnson = 'https://www.imdb.com/name/nm0425005/'
    chris_hemsworth = 'https://www.imdb.com/name/nm1165110/'
    robert_downey_jr = 'https://www.imdb.com/name/nm0000375/'
    akshay_kumar = 'https://www.imdb.com/name/nm0474774/'
    jackie_chan = 'https://www.imdb.com/name/nm0000329/'
    bradley_cooper = 'https://www.imdb.com/name/nm0177896/'
    adam_sandler = 'https://www.imdb.com/name/nm0001191/'
    scarlett_johansson = 'https://www.imdb.com/name/nm0424060/'
    sofia_vergara = 'https://www.imdb.com/name/nm0005527/'
    chris_evans = 'https://www.imdb.com/name/nm0262635/'

    # stallone = 'https://www.imdb.com/name/nm0000230/'
    # mei_yong = 'https://www.imdb.com/name/nm3619308/'

    actors = [dwayne_johnson, chris_hemsworth, robert_downey_jr, akshay_kumar,
              jackie_chan, bradley_cooper, adam_sandler,
              scarlett_johansson, sofia_vergara, chris_evans]

    # perm2 = []
    # for i in range(len(actors)):
    #     for j in range(i+1, len(actors)):
    #         if i == j:
    #             continue
    #
    #         a = actors[i]
    #         b = actors[j]
    #         perm2.append((a, b))
    #
    # import random
    # random.shuffle(perm2)

    # print(get_movie_distance(
    #     dwayne_johnson,
    #     'https://www.imdb.com/name/nm0542677/' # Byron Mann
    # ))

    # should be 2
    # print(get_movie_distance(
    #     dwayne_johnson,
    #     'https://www.imdb.com/name/nm0571964/' # Ray MacKinnon
    # ))

    # print(get_movie_distance(dwayne_johnson, chris_hemsworth))
    # print(get_movie_distance(dwayne_johnson, akshay_kumar))
    # print(get_movie_distance(dwayne_johnson, jackie_chan))
    # print(get_movie_distance(chris_hemsworth, jackie_chan))

    # print(get_movie_distance(stallone, mei_yong))

    # sol = {}
    # for a, b in perm2:
    #     sol[(a, b)] = get_movie_distance(a, b, 1)
    #     sol[(b, a)] = get_movie_distance(b, a, 1)
    #
    # print(sol)

    name_to_url = {
        'dwayne_johnson': 'https://www.imdb.com/name/nm0425005/',
        'chris_hemsworth': 'https://www.imdb.com/name/nm1165110/',
        'robert_downey_jr': 'https://www.imdb.com/name/nm0000375/',
        'akshay_kumar': 'https://www.imdb.com/name/nm0474774/',
        'jackie_chan': 'https://www.imdb.com/name/nm0000329/',
        'bradley_cooper': 'https://www.imdb.com/name/nm0177896/',
        'adam_sandler': 'https://www.imdb.com/name/nm0001191/',
        'scarlett_johansson': 'https://www.imdb.com/name/nm0424060/',
        'sofia_vergara': 'https://www.imdb.com/name/nm0005527/',
        'chris_evans': 'https://www.imdb.com/name/nm0262635/',
    }

    for name, url in name_to_url.items():
        actor_page = requests.get(url, headers=hf.HEADERS)
        actor_page_soup = BeautifulSoup(actor_page.text, features="html.parser")
        descs = get_movie_descriptions_by_actor_soup(actor_page_soup)
        with open('week12/' + name + '.txt', 'w') as f:
            f.writelines(descs)
