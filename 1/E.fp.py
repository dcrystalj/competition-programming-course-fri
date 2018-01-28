from collections import Counter
n, k = map(long, raw_input().split())
nums = map(long, raw_input().split())
nums.sort()
k -= 1
first = nums[k/n]
c = Counter(nums)
i = 0
while c[nums[i]] * n < k+1:
    k -= c[nums[i]] * n
    j = nums[i]
    while nums[i] == j:
        i += 1

second = nums[k / c[nums[i]]]

print str(first) + ' ' + str(second)
