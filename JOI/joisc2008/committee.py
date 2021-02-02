# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# https://www.ioi-jp.org/camp/2008/2008-sp-tasks/2008-sp_tr-day1_20.pdf
# 検討15分　実装15分 バグとり15分
# 桁DPできそうと思いながら他の解法を探してしまった。
# 桁DPはライブラリ化しているので、実装に15分もかけているのはダメ

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# 前準備
import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]
score = [0]*(n+1)
for i in range(1,n+1):
    a,b = map(int,input().split())
    if(a!=0):
        graph[a].append(i)
        graph[i].append(a)
    score[i] = b

max_ = max(score[1:])
if(max_ <= 0):
    print(max_)
    exit()

ini = 0

# calcの定義 : 2辺を合わせる演算
def calc(a,b):
    return a+b

# dp1の更新
def calc1(c,p):
    #############
    # ここにいい感じに定義
    #############

    p_num = ini
    for i in graph[c]:
        if i == p:
            continue
        p_num = calc(p_num, dp1[i])
    dp1[c] = max(0, p_num+score[c])

# dp2の更新　累積和チックにすることでうに対策。
def calc2(p):
    #############
    # ここにいい感じに定義
    #############
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
        prod.append( calc(a,b) )

    for c,x in zip(graph[p], prod):
        if(c != parent[p]):
            dp2[c] = max(0, x+score[p])



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
dp1 = [0] * (n+1)
for i in order[::-1]:
    calc1(i, parent[i])

# 子→親の値を算出
dp2 = [0] * (n+1)
for i in order:
    calc2(i)


ans = max(score[1:])
for i in range(1,n+1):
    ans = max(ans,dp1[i]+dp2[i])
print(ans)
