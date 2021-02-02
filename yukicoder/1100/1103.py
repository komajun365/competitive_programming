# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
ab = list(map(int,read().split()))
mod = 10**9 + 7

it = iter(ab)
root = (n+1)*n//2
parent = [0] * (n+1)
links = [[] for _ in range(n+1)]
for a,b in zip(it,it):
    links[a].append(b)
    parent[b] = a
    root -= b

tp = [root]
stack = [root]
while(stack):
    next = []
    while(stack):
        i = stack.pop()
        for j in links[i]:
            next.append(j)
            tp.append(j)
    stack = next[::]

score = [[0,0] for _ in range(n+1)]

ans = 0
for i in tp[::-1]:
    ans += score[i][0]
    par = parent[i]
    score[par][0] += score[i][0] + score[i][1] + 1
    score[par][0] %= mod
    score[par][1] += score[i][1] + 1


print(ans%mod)

'''
葉からはどこにもいけない。

ある頂点から行けるパスの長さ合計がx,行ける頂点の数がyだとしたら、
その親に対して、長さ(x+y+1),頂点(y+1)貢献できる。

トポロジカル！
根を教えてくれないなんてけちですね。

'''
