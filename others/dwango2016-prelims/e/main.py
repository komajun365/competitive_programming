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

n,l,*tp = map(int,read().split())

now = -1
p_list = []
it = iter(tp)
for t,p in zip(it,it):
    if now == t:
        p_list[-1].append(p)
    else:
        p_list.append([p])
        now = t

hq_l = []
hq_r = []

def add(x):
    left = hq_l[-1]
    right = hq_r[-1]
    if len(left) == 0:
        left.append(x*-1)
    else:
        if len(left) == len(right):
            if right[0] >= x:
                heappush(left, x*-1)
            else:
                y = heappop(right)
                heappush(right, x)
                heappush(left, y*-1)
        else:
            if left[0] * -1 <= x:
                heappush(right, x)
            else:
                y = heappop(left)*-1
                heappush(left, x*-1)
                heappush(right, y)

while p_list:
    ps = p_list.pop()
    hq_l.append([])
    hq_r.append([])
    for p in ps:
        add(p)
    while len(hq_l) > 1:
        if hq_l[-1][0] >= hq_l[-2][0]:
            break
        l1 = hq_l.pop()
        r1 = hq_r.pop()
        if len(l1) + len(r1) > len(hq_l[-1]) + len(hq_r[-1]):
            l2 = hq_l.pop()
            r2 = hq_r.pop()
            l1,l2 = l2,l1
            r1,r2 = r2,r1
            hq_l.append(l2)
            hq_r.append(r2)
        for p in l1:
            add(p*-1)
        for p in r1:
            add(p)

ans = 0
for left,right in zip(hq_l,hq_r):
    x = left[0] * -1
    ans += x * len(left) + sum(left) + sum(right) - x * len(right)
print(ans)

