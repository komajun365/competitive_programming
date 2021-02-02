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
data = list(map(int,read().split()))

links = [[] for _ in range(n+1)]
it = iter(data)
for ai,bi in zip(it,it):
    links[ai].append(bi)
    links[bi].append(ai)

links[0].append(1)
links[1].append(0)

tp = []
parent = [-1] * (n+1)
stack = [0]
while(stack):
    i = stack.pop()
    for j in links[i]:
        if(parent[i]==j):
            continue
        parent[j] = i
        stack.append(j)
        tp.append(j)

tp = tp[::-1]
come = [[] for _ in range(n+1)]

for i in tp:
    if(len(come[i])==0):
        # print(i)
        # print(parent[i])
        # print(a[i])
        # print(come[parent[i]])
        # print('--')
        come[parent[i]].append(a[i])
        continue

    up = 2*a[i] - sum(come[i])
    if(up < 0)|(max(up,max(come[i])) > a[i]):
        print('NO')
        exit()
    come[parent[i]].append(up)

# print(come)

if(len(come[1]) > 1)&(come[0][0] == 0):
    print('YES')
elif(len(come[1]) == 1)&(come[0][0] == a[1]):
    print('YES')
else:
    print('NO')
