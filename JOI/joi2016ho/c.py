# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討17分　実装40分 バグとり30分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,q= map(int,readline().split())
data = list(map(int,read().split()))
r = data[2*m:]
r_rev = [q+1] * m
for i,ri in enumerate(r,1):
    r_rev[ri-1] = i

links = [[] for _ in range(n+1)]
for i in range(m):
    a,b = data[i*2:i*2+2]
    up = r_rev[i]
    links[a].append((b,up))
    links[b].append((a,up))

inf = n*10
stop = [(inf,q+1)] * (n+1)

stack = []
stack2 = [(1,q+1)]

for i in range(n):
    if(not stack2):
        break

    stack = stack2[::]
    stack2 = []
    news = set()

    while(stack):
        town,ri = stack.pop()
        if(stop[town][0] < i):
            continue
        if(stop[town][0]==i)&(stop[town][1] >= ri):
            continue
        stop[town] = (i, ri)
        news.add(town)

    for town in news:
        ri = stop[town][1]
        for j,rj in links[town]:
            if(stop[j][0] != inf):
                continue
            stack2.append((j, min(ri,rj)))

ans = [0] * (q+1)
for i,j in stop[2:]:
    if(j!=q+1):
        ans[j] += 1

for i in range(q):
    ans[i+1] += ans[i]

print('\n'.join(map(str,ans[1:])))


print(stop)


'''
幅優先探索。
コストが同じならば、
i年後に値上げするRiの道を通らないルートを優先する。
通らないといけない場合、通る中でのiがなるべく大きいルートを優先する。

適当にやり過ぎてバグまつり。。。

'''
