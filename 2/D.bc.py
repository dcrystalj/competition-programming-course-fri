import sys
n = int(input())
states = [list(map(int, input().split())) for _ in range(n)]

def time(a, b):
    return -(a[0] - z(a,b)) / a[1]
def z(a, b):
    s1, v1 = a
    s2, v2 = b
    print (a, b)
    return (v1 * s2 - v2 * s1) / (-v2 + v1)

if n == 1:
    print (-1)
    sys.exit()

minimum = 10000000001
for i in range(n):
    for j in range(i+1,n):
        x = states[i]
        y = states[j]

        if x[1] > 0 and y[1] > 0 or \
            x[1] < 0 and y[1] < 0:
            continue

        t = time(x, y)
        print ("timer", t, i, j, i!=j)
        if t < minimum and t >= 0 and i != j:
            minimum = t

if minimum == 10000000001:
    print (-1)
else:
    print (minimum)