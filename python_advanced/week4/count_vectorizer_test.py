from count_vectorizer import CountVectorizer


corpus = [
    'AATACAT',  # 'AA', 'AT', 'TA', 'AC', 'CA', 'AT'
    'CTACCCT',  # 'CT', 'TA', 'AC', 'CC', 'CC', 'CT'
    'TACCTAC',  # 'TA', 'AC', 'CC', 'CT', 'TA', 'AC'
]

cv = CountVectorizer(2)
cv.fit(corpus)
print(cv.d)
print(cv.transform(corpus))
print(cv.fit_transform(corpus))


corpus = [
    'AATACAT',  # 'AA', 'AT', 'TA', 'AC', 'CA', 'AT'
    'CTACCCT',  # 'CT', 'TA', 'AC', 'CC', 'CC', 'CT'
    'TACCTAC',  # 'TA', 'AC', 'CC', 'CT', 'TA', 'AC'
]

correct_transformation = [
    [1, 1, 2, 1, 0, 0, 1],
    [0, 1, 0, 0, 2, 2, 1],
    [0, 2, 0, 0, 1, 1, 2],
]

# case 1
vectorizer = CountVectorizer(ngram_size=2)
vectorizer.fit(corpus)
print(vectorizer.transform(corpus) == correct_transformation)  # True

# case 2
vectorizer = CountVectorizer(ngram_size=2)
print(vectorizer.fit_transform(corpus) == correct_transformation)  # True

# case 3
corpus_2 = ['TCAATCAC', 'GGGGGGGGGGG', 'AAAA']
vectorizer = CountVectorizer(ngram_size=2)
vectorizer.fit(corpus)
print(vectorizer.d)
print(vectorizer.transform(corpus_2))
print(vectorizer.transform(corpus_2) == [
    [1, 1, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [3, 0, 0, 0, 0, 0, 0]
])  # True
