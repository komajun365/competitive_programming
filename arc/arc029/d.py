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
data = list(map(int,read().split()))
s = data[:n]
ab = data[n:n+2*(n-1)]
m = data[n+2*(n-1)]
t = data[n+2*(n-1)+1:]
inf = 10**15

links = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

min_select = [[] for _ in range(n+1)]
tp = []
stack = [1]
while(stack):
    i = stack.pop()
    tp.append(i)
    for j in links[i]:
        if(j<i):
            continue
        stack.append(j)

tp = tp[::-1]
for i in tp:
    size = 1
    for j in links[i]:
        if(j<i):
            continue
        size += len(min_select[j])
    min_select[i] = [inf] * size
    min_select[i][0] = s[i-1]

    for j in links[i]:
        if(j<i):
            continue

        for k in range()




'''
87653321

根を含むサイズkの部分木を、
tの上位k個に置き換えることができる。

→　サイズkを決めたときに、最小得点の部分木（あるいはその合計点）がわかればいい。



'''
