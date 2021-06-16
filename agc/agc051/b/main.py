# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

n = 23
nums = [1]
for i in range(1,n+1):
    nums.append(nums[-1] + i)

nums2 = nums[1:] + [nums[-1]+1]
# print(nums)
# print(nums2)

xy = []
for k in range(20):
    base = 300 * k
    for i in range(n):
        x = nums[i] + base
        for y in range(n):
            xy.append([x, nums2[y]+base])

a = set()
b = set()
b_cnt = dict()
c = set()
d = set()
for x,y in xy:
    a.add(x)
    b.add(x-y)
    c.add(y)
    d.add(x+y)
    if x-y in b_cnt:
        b_cnt[x-y] += 1
    else:
        b_cnt[x-y] = 1

# print(len(a),len(b),len(c),len(d))
print(len(xy))
print('\n'.join(map(lambda x: ' '.join(map(str,x)),xy)))