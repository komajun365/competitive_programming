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


import sys
read = sys.stdin.buffer.read
from heapq import heappop,heappush

n,Q,*q = map(int,read().split())

lis = [n]
for qi in q:
    while lis:
        if lis[-1] >= qi:
            lis.pop()
        else:
            lis.append(qi)
            break
    else:
        lis.append(qi)

d = dict()
d[lis[-1]] = 1
hq = [-1 * lis[-1]]
l = len(lis)

for i in range(l-1,0,-1):
    a = lis[i-1]
    b = lis[i]
    while hq[0] < a * -1:
        num = heappop(hq) * -1
        x,y = divmod(num,a)
        if x > 0:
            if a in d:
                d[a] += d[num] * x
            else:
                d[a] = d[num] * x
                heappush(hq,a*-1)
        if y > 0:
            if y in d:
                d[y] += d[num]
            else:
                d[y] = d[num]
                heappush(hq, y*-1)
        del d[num]

ans = [0] * (n+1)
for key,val in d.items():
    ans[key] += val

for i in range(n,0,-1):
    ans[i-1] += ans[i]

print('\n'.join(map(str,ans[1:])))




# imos = [0] * (n+1)
# l = len(lis)
# hq = [ -1 * ((lis[-1] <<30) + 1) ]

# for i in range(l-1,0,-1):
#     a = lis[i]
#     b = lis[i+1]
#     for j in range(b,a,-1):
#         imos[j % a] += imos[j]
#         imos[a] += imos[j]//a
#         imos[j] = 0

# print(imos)




