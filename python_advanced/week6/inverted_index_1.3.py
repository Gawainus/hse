class InvertedIndex:
    def __init__(self, word_to_docs_mapping):
        self.m = word_to_docs_mapping

    def query(self, words):
        combined = set()
        for w in words:
            s = self.m.get(w, set())
            combined.update(s)
        return combined


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

    return InvertedIndex(d)

# ld = load_document('arts.txt')
# print(build_inverted_index(ld).query(['Java', 'an']))
