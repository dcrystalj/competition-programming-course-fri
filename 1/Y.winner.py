from collections import defaultdict
n = int(raw_input())
scores = [raw_input().split() for _ in range(n)]

states = []
scoreboard = defaultdict(int)

for i,j in scores:
    scoreboard[i] += int(j)
    states.append([i,scoreboard[i]])

m = max(scoreboard.values())
for i,j in states:
    if j>=m and scoreboard[i] == m:
        print i
        break