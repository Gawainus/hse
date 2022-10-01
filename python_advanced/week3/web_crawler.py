import json
from datetime import datetime


def flatten_data(y):
    out = []

    def flatten(x, name=''):
        if type(x) is dict and bool(x):
            for k, v in x.items():
                flatten(v, name + k + '/')
        else:
            out.append(name[:-1])

    flatten(y)
    return out


file = input()
with open(file, 'r') as f:
    for ln in f:
        j = json.loads(ln)
        a = flatten_data(j)
        print('\n'.join(sorted(a)))
