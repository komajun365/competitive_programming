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


n = int(input())
p = list(map(int,input().split()))

links = [[] for _ in range(1 + n**2)]
for i in range(n):
    for j in range(n):
        x = i*n+j + 1
        if(i!=0):
            links[x].append(x-n)
        if(i!=n-1):
            links[x].append(x+n)
        if(j!=0):
            links[x].append(x-1)
        if(j!=n-1):
            links[x].append(x+1)
        if(i==0)|(i==n-1)|(j==0)|(j==n-1):
            links[x].append(0)

sit = [1] * (1+n**2)
sit[0] = 0

def dfs(links,start,goal,m):
    cost = [-1]*m
    stack = [[start],[]]
    cost[start] = 0
    for depth in range(n+10):
        while(stack[depth%2]):
            now = stack[depth%2].pop()
            for y in links[now]:
                if(cost[y] == -1):
                    cost[y] = depth + sit[y]
                    stack[cost[y]%2].append(y)

        if(cost[goal] != -1):
            return cost[goal]

ans = 0
for x in p:
    sit[x] = 0
    ans += dfs(links,x,0,n**2+1)

print(ans)
