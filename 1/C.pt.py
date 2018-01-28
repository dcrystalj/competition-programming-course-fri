t = raw_input().split(':')
h2 = int(t[0][0])
h1 = int(t[0][1])
m2 = int(t[1][0])
m1 = int(t[1][1]) + 1
print h1,h2,m1,m2
while (h2 != m1 or h1 != m2):
    if (m1 == 10):
        m1 = 0
        m2 += 1
    if (m2 == 6):
        m2 = 0
        h1 += 1
    if (h1 == 10 and h2 < 2):
        h1 = 0
        h2 += 1
    if (h1 == 4 and h2 == 2):
        h2 = 0
        h1 = 0

    #check palindrom
    if (h1 == m2 and h2 == m1):
        break

    m1 += 1

print str(h2) + str(h1) + ":" + str(m2) + str(m1)
