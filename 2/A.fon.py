n, k = map(int, raw_input().split())
states = [(raw_input().split()) for i in range(n)]
friends = []
for i,j,m in states:
    for x,y,z in states:
        if x == j and y == i and int(z) - int(m) <= k \
            and int(z) > int(m):
            friends.append((i, j))

#remove dups
friends = list(set(friends))
i = 0
while i < len(friends):
    j = friends[i]
    if (j[1], j[0]) in friends:
        friends.pop(i)
    else:
        i+=1

print len(friends)
for i,j in friends:
    print i + ' ' + j