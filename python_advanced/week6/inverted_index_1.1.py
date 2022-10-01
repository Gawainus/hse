# def load_document(filepath):
#     d = dict()
#     with open(filepath, mode='r', encoding='utf-8') as f:
#         for ln in f:
#             tks = ln.split('\t')
#             d[int(tks[0])] = tks[1]
#     return d


def load_document(filepath):
    articles = dict()
    with open(filepath, mode='r', encoding='utf-8') as f:
        for ln in f:
            tks = ln.split('\t')
            _id = int(tks[0])
            rest = tks[1]
            articles.update({int(_id): rest.strip()})
    return articles


# ld = load_document('wikipedia_sample.txt')
# print(ld)
