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

from math import gcd

n = int(input())
a = list(map(int,input().split()))

min_a = min(a)
cand = dict()
for ai in a:
    tmp = []
    for i in range(1,10**5):
        if i > min_a or i**2 > ai:
            break
        if ai % i == 0:
            tmp.append(i)
            j = ai//i
            if i != j and j <= min_a:
                tmp.append(j)
        
    for j in tmp:
        if j in cand:
            cand[j] = gcd(cand[j], ai)
        else:
            cand[j] = ai

ans = 0
for k,v in cand.items():
    if k == v:
        ans += 1

print(ans)
# print(cand)


# nums = set()
# hq = []
# for ai in a:
#     heappush(hq, ai*-1)
#     nums.add(ai)

# while(hq):
#     i = heappop(hq)
#     i *= -1
#     nums_add = []
#     for hi in hq:
#         tmp = gcd(i,hi*-1)
#         if not tmp in nums:
#             nums.add(tmp)
#             nums_add.append(tmp)
    
#     for j in nums_add:
#         heappush(hq,j)

# ans = 0
# for num in nums:
#     if num <= min_a:
#         ans += 1
# print(ans)

# print(nums)
