class CountVectorizer:
    def __init__(self, ngram_size):
        self.ngram_size = ngram_size
        self.d = dict()

    def fit(self, corpus):
        self.d = dict()
        s = set()
        for row in corpus:
            n = len(row) - self.ngram_size + 1
            for i in range(0, n):
                t = row[i: i + self.ngram_size]
                s.add(t)

        s = sorted(s)
        for i, t in enumerate(s):
            self.d[t] = i

    def transform(self, corpus):
        transformed_corpus = list()
        for row in corpus:
            occur_d = dict()
            n = len(row) - self.ngram_size + 1
            for i in range(0, n):
                t = row[i: i + self.ngram_size]
                if t not in occur_d:
                    occur_d[t] = 0

                occur_d[t] += 1

            c_row = list()
            for k in self.d.keys():
                c_row.append(occur_d.get(k, 0))

            transformed_corpus.append(c_row)

        return transformed_corpus

    def fit_transform(self, corpus):
        self.fit(corpus)
        return self.transform(corpus)
