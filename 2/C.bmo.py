import math
n, k = map(int, input().split())
q = 1/k
q20 = q**40
f = (1-q20) / (1-q)
if k > n:
    print (1)
else:
    for i in range(int(n/2),10000000000):
        a = i * f
        if a > n:
            summer = int(i)
            tmp = summer
            while tmp >= k:
                a = int(tmp / k)
                summer += a
                tmp = a
            if summer >= n:
                print(i)
                break