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
a = [0] + list(map(int,readline().split()))
b = [0] + list(map(int,readline().split()))
if(n==1):
    print(max(0,a[1]))
    exit()
data = list(map(int,read().split()))

links = [[] for _ in range(n+1)]
it = iter(data)
for u,v in zip(it,it):
    links[u].append(v)
    links[v].append(u)

stack = [1]
done = [0] * (n+1)
done[1] = 1
tp = []
child = [[] for _ in range(n+1)]
while(stack):
    i = stack.pop()
    tp.append(i)
    for j in links[i]:
        if(done[j] == 1):
            continue
        done[j] = 1
        child[i].append(j)
        stack.append(j)

scores = [[0,0] for _ in range(n+1)]

for i in tp[::-1]:
    for j in child[i]:
        scores[i][0] += max(scores[j][0] + b[i] + b[j], scores[j][1])
        scores[i][1] += max(scores[j])
    scores[i][1] += a[i]

print(max(scores[1]))
