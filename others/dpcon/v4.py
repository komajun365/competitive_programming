# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
mod = m
# mod = 10**9+7

# 前準備
import sys
input = sys.stdin.readline
from collections import deque

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ini = 1

def calc(a,b):
    p = a * b % mod
    return p

# calc1 の定義
def calc1(c,p):
    p_num = ini
    for i in graph[c]:
        if i == p:
            continue
        p_num = calc(p_num, dp1[i])
    p_num += 1
    dp1[c] = p_num % mod

# calc2 の定義
def calc2(p):
    arr = [dp1[c] if c != parent[p] else dp2[p] for c in graph[p]]

    left = [ini]
    for i in arr[:-1]:
        left.append( calc(left[-1], i ) )
    right = [ini]
    for i in arr[:0:-1]:
        right.append( calc(right[-1], i) )
    right = right[::-1]

    prod = []
    for a,b in zip(left,right):
        prod.append(calc(a,b))

    for c,x in zip(graph[p], prod):
        if(c != parent[p]):
            dp2[c] = (x + 1)%mod



# 根から探索して親と探索順を記録
root = 1
order = []
parent = [0] * (n+1)
stack = deque()
stack.append(root)
while stack:
    x = stack.pop()
    order.append(x)
    for y in graph[x]:
        if y == parent[x]:
            continue
        stack.append(y)
        parent[y] = x

# 親→子の値を算出
dp1 = [None] * (n+1)
for i in order[::-1]:
    calc1(i, parent[i])

# 子→親の値を算出　累積和チックにすることでうに対策。
dp2 = [None] * (n+1)
dp2[root] = ini
for i in order:
    calc2(i)

for i in range(1,n+1):
    ans = calc(dp1[i]-1, dp2[i])
    print(ans)

print(dp1)
print(dp2)
