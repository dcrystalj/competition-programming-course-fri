from collections import defaultdict
n = int(raw_input())
scores = [raw_input().split() for _ in range(n)]
max_score = [scores[0][0], 0]

scoreboard = defaultdict(int)
max_scoreboard = defaultdict(lambda: [0, 0])
c = 0

for i,j in scores:
    scoreboard[i] += int(j)

    if max_score[1] < scoreboard[i]:
        max_score = [i, scoreboard[i]]

    if max_scoreboard[i][0] < scoreboard[i]:
        max_scoreboard[i] = [scoreboard[i], c]

    c += 1


d = dict(scoreboard)
m = max(d, key=lambda x: d[x])
max_val = d[m]

if (d[max_score[0]] < max_val):
    s = sorted(max_scoreboard.keys(), key= lambda x: max_scoreboard[x][1])
    print [i for i in s if max_scoreboard[i][0] == max_val][0]
else:
    print max_score[0]