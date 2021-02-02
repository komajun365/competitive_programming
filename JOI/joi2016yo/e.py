# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討6分　実装20分 バグとり7分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,m,k,s = map(int,readline().split())
p,q = map(int,readline().split())
data = tuple(map(int,read().split()))
c = data[:k]
ab = data[k:]

links = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links[a].append(b)
    links[b].append(a)

stack = [list(c),[]]
city = [-1] * (n+1)
for i in c:
    city[i] = 0

for i in range(s):
    st = stack[i%2]
    while(st):
        now = st.pop()
        for j in links[now]:
            if(city[j] == -1):
                stack[(1+i)%2].append(j)
                city[j] = i+1

city = [ p if i ==-1 else q if i>0 else 10**10 for i in city]
city[-1] = 0

links2 = [[] for _ in range(n+1)]
it = iter(ab)
for a,b in zip(it,it):
    links2[a].append((city[b],b))
    links2[b].append((city[a],a))

# dijkstra
import heapq
def dijkstra(links, start, n):
    inf = 10**10
    d = [inf] * (n)
    d[start] = 0
    hq = []
    for i in links[start]:
        heapq.heappush(hq, i)
    while(hq):
        cost,i = heapq.heappop(hq)
        if( d[i] != inf):
            continue
        d[i] = cost
        for tmp in links[i]:
            cost_next, j = tmp
            if(d[j] == inf):
                heapq.heappush(hq, (cost+cost_next, j))
    return d

d = dijkstra(links2,1,n+1)
print(d[-1])


'''
まず、危険な街とそうでない町の判定を行う。
これはBFSでO(M)で判定可能。

次に、行った先の町の宿泊費が通過コストとなるようにエッジを整理する。
(支配された町の場合はコストinf)。O(M)
そのあとで町１を起点としたダイクストラを実行する。
O(MlogM)

'''
