import json
from datetime import datetime

files = input().split()
o_file = input()
d = dict()


def parse(file_path):
    with open(file_path, 'r') as f:
        for ln in f:
            j = json.loads(ln)
            k = (datetime.strptime(j['date'], "%Y-%m-%d %H:%M:%S"),
                 j['consumer_id'])

            d[k] = j['message']


for f in files:
    parse(f)


with open(o_file, 'w') as o:
    for k, v in sorted(d.items()):
        ln = f'{datetime.strftime(k[0], "%Y-%m-%d %H:%M:%S")}\t{v}\n'
        o.write(ln)
