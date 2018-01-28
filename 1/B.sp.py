n = int(raw_input())
b = [map(int, raw_input().split()) for i in range(n)]
superset = 0

for i in b:
    l = u = d = r = False
    for j in b:
        if (i[0] > j[0] and i[1] == j[1]): r = True
        if (i[0] < j[0] and i[1] == j[1]): l = True
        if (i[0] == j[0] and i[1] < j[1]): d = True
        if (i[0] == j[0] and i[1] > j[1]): u = True
    if (r and l and d and u): superset += 1

print superset