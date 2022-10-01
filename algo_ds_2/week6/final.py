

def count_discusibility(movies, friends):
    """
    we count through the movie list of each friend
    Runtime: len(friends) * len(movies)
    :param movies:
    :param friends:
    :return: a dictionary of movie to friends (discusibility)
    """
    d = {m: 0 for m in movies}
    for f in friends:
        for m in f:
            d[m] += 1

    return d


def calc_uniqueness(movies, similarities, discu):
    """
    Let the number of movies be `n`

    :param movies: list of movies
    :param similarities: pairs of similar movies
    :param discu: discusibility calculated above
    :return:
    """

    # We first need to put the similarity pairs into clusters since there is
    # a transitive property
    clusters = []
    for p in similarities:
        fir = p[0]
        sec = p[1]
        added = False
        for c in clusters:
            if fir in c or sec in c:
                c.add(fir)
                c.add(sec)
                added = True

        if not added:
            clusters.append(set(p))

    """
    Let k be the size of each cluster. Sum of k equals to n.
    So this 3 loop's runtime is <= n^2
    """
    d_sim = {m: [] for m in movies}
    for c in clusters:
        for m in c:
            for sim in c:
                if sim == m:
                    continue

                d_sim[m].append(discu[sim])

    return d_sim


def recommend(movies, similarities, friends):
    discu = count_discusibility(movies, friends)
    uniqu = calc_uniqueness(movies, similarities, discu)

    from numpy import mean
    scores = [discu[m] / mean(uniqu[m]) if mean(uniqu[m]) != 0 else 0 for m in movies]
    rec = max(scores)
    return movies[scores.index(rec)]


if __name__ == '__main__':
    movies = ["Parasite", "1917", "Ford v Ferrari", "Jojo Rabbit", "Joker"]

    similarities = [["Parasite", "1917"],
                    ["Parasite", "Jojo Rabbit"],
                    ["Joker", "Ford v Ferrari"]]

    friends = [["Joker"],
               ["Joker", "1917"],
               ["Joker"],
               ["Parasite"],
               ["1917"],
               ["Jojo Rabbit", "Joker"]]

    print(recommend(movies, similarities, friends))
