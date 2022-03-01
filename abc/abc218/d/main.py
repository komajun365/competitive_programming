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

n,*xy = map(int,read().split())

point = dict()
it = iter(xy)
for x,y in zip(it,it):
    if x in point:
        point[x].append(y)
    else:
        point[x] = [y]

cnt = dict()
for ys in point.values():
    l = len(ys)
    if l < 2:
        continue
    for i in range(l-1):
        a = ys[i]
        for j in range(i+1,l):
            b = ys[j]
            idx = (min(a,b) << 30) + max(a,b)
            cnt[idx] = cnt.get(idx,0) + 1

ans = 0
for ci in cnt.values():
    ans += ci*(ci-1)//2
print(ans)

# print(point)