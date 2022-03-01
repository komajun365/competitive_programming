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

n,*data = map(int,read().split())
a = data[:n]
uv = [i-1 for i in data[n:]]

links = [[] for _ in range(n)]
it = iter(uv)
for u,v in zip(it,it):
    links[u].append(v)
    links[v].append(u)

left = []
right = []
l_del = []
r_del = []
l_size = 0
r_size = 0

def gabage():
    while l_del:
        if l_del[0] == left[0]:
            heappop(l_del)
            heappop(left)
        else:
            break
    while r_del:
        if r_del[0] == right[0]:
            heappop(r_del)
            heappop(right)
        else:
            break

def add(x):
    gabage()
    global l_size, r_size
    if l_size == 0:
        heappush(left, x*-1)
        l_size += 1
    elif l_size > r_size:
        if left[0] * -1 <= x:
            heappush(right, x)
        else:
            y = heappop(left) * -1
            heappush(right, y)
            heappush(left, x*-1)
        r_size += 1
    else:
        if right[0] < x:
            y = heappop(right)
            heappush(right, x)
            heappush(left, y*-1)
        else:
            heappush(left, x*-1)
        l_size += 1

def delete(x):
    gabage()
    global l_size, r_size
    if left[0] * -1 >= x:
        heappush(l_del, x*-1)
        gabage()
        if l_size == r_size:
            y = heappop(right)
            heappush(left, y*-1)
            r_size -= 1
        else:
            l_size -= 1
    else:
        heappush(r_del, x)
        gabage()
        if l_size != r_size:
            y = heappop(left) * -1
            heappush(right, y)
            l_size -= 1
        else:
            r_size -= 1

def calc():
    gabage()
    if l_size > r_size:
        return left[0] * -1
    else:
        return (left[0] * -1 + right[0])//2

dp = [-1] * n
depth = [-1] * n
parent = [-1] * n
depth[0] = 0
parent[0] = -2


stack = [~0,0]
while stack:
    i = stack.pop()
    if i >= 0:
        add(a[i])
        for j in links[i]:
            if depth[j] != -1:
                continue
            depth[j] = depth[i] + 1
            parent[j] = i
            stack.append(~j)
            stack.append(j)
    else:
        i = ~i
        if i != 0 and len(links[i]) == 1:
            dp[i] = calc()
        else:
            if depth[i] % 2 == 0:
                num = 0
                for j in links[i]:
                    if j == parent[i]:
                        continue
                    num = max(num, dp[j])
                dp[i] = num
            else:
                num = 10**10
                for j in links[i]:
                    if j == parent[i]:
                        continue
                    num = min(num, dp[j])
                dp[i] = num
        delete(a[i])

print(dp[0])





        


