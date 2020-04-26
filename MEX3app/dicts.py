'''Contains dictionaries used in backend and templates'''

import string

res = []   # dict for column names

for n, s in enumerate(string.ascii_uppercase):
    res.append((n + 1, s))

res_row = []   #dict for row nums

for i in range(1, 500):
    res_row.append((i, i))
