import sys
from collections import Counter
a = list(input())
b = list(input())
c = Counter(b)
d = ['9','8','7','6','5','4','3','2','1']

for i,j in enumerate(a):
    while c[d[0]] == 0:
        e = d.pop(0)
        if e == '1':
            print("".join(a))
            sys.exit()

    if j < d[0]:
        a[i] = d[0]
        c[d[0]] -= 1


print("".join(a))