from itertools import chain, combinations
l1, l2 = map(int, raw_input().split())
a = map(int, raw_input().split())
b = map(int, raw_input().split())
a = a + a[:-1]
b = b + b[:-1]
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


c = [i for i in powerset(a)]
d = [i for i in powerset(b)]
e = [i for i in c if i in d]
print e