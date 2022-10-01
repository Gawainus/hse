def load_document(filepath):
    d = dict()
    with open(filepath, mode='r', encoding='utf-8') as f:
        for ln in f:
            tks = ln.split('\t')
            _id = int(tks[0])
            rest = tks[1]
            d.update({int(_id): rest.strip()})
    return d


def build_inverted_index(articles):
    d = dict()
    for k, v in articles.items():
        tks = v.split()
        for t in tks:
            d.setdefault(t, set())
            d[t].add(k)

    return d


# ld = load_document('arts.txt')
# print(build_inverted_index(ld))
