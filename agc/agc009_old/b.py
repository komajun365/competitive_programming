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
a = [0,0] + list(map(int,read().split()))
child = [[] for _ in range(n+1)]

for i,ai in enumerate(a[2:],2):
    child[ai].append(i)

stack = [1]
tp = []
while(stack):
    i = stack.pop()
    tp.append(i)

    for j in child[i]:
        stack.append(j)

cost = [[] for _ in range(n+1)]
for i in tp[::-1]:
    if(len(cost[i])==0):
        cost[a[i]].append(0)
        continue

    cost_i = sorted(cost[i], reverse=True)
    for j in range(len(cost_i)):
        cost_i[j] += j+1
    cost[a[i]].append(max(cost_i))

print(cost[0][0])

print(cost)



'''
誰が何試合したか、はわかる。

1を親にして木を作る
ある葉に子供がx人いる場合、




'''
