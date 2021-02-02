import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f


n = int(input())
ab = [list(map(int, input().split())) for _ in range(n-1)]
c = list(map(int,input().split()))

edge_num = [0] * (n+1)
edge = {}
for i in range(1,n+1):
    edge[i] = set()

for a,b in ab:
    edge_num[a] += 1
    edge_num[b] += 1
    edge[a].add(b)
    edge[b].add(a)

edge_num2 = {}
for i in range(max(edge_num) + 1):
    edge_num2[i] = set()

for i in range(1,n+1):
    edge_num2[edge_num[i]].add(i)

c = sorted(c)
c_num = 0
ans = [0] * (n+1)
while(len(edge_num2[1]) > 0):
    tmp = edge_num2[1].pop()
    ans[tmp] = c[c_num]
    c_num += 1

    neigh = edge[tmp].pop()
    edge_num2[edge_num[neigh]].discard(neigh)
    edge_num[neigh] -= 1
    edge_num2[edge_num[neigh]].add(neigh)
    edge[neigh].discard(tmp)
    if(edge_num[neigh] == 0):
        ans[neigh] = c[c_num]
        break

print(sum(c) - max(c))
print(' '.join(map(str, ans[1:])))
