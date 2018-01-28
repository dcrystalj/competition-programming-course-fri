n, k = map(long, raw_input().split())
operations = [raw_input().split() for _ in range(n)]


def defragment(arr, k):
    b = [ arr[i] for i in range(k) if arr[i] != 0]
    while(len(b) < k):
        b.append(0)
    return b

def erase(arr, x):
    if x in arr and x > 0:
        for i in range(len(arr)):
            if arr[i] == x:
               arr[i] = 0
    else:
        print "ILLEGAL_ERASE_ARGUMENT"

def alloc(arr, n, x): #x = identifier
    zeros = [0 for i in range(n)]
    for i in range(len(arr)):
        if arr[i:i+n]==zeros:
            arr[i:i+n] = [x for j in range(n)]
            print x
            return x+1

    print "NULL"
    return x

arr = [0 for i in range(k)]
x = 1
for i in operations:
    if i[0] == "alloc":
        x = alloc(arr, int(i[1]), x)
    elif i[0] == "erase":
        erase(arr, int(i[1]))
    else:
        arr = defragment(arr, k)
    #print arr