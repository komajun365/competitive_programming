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

x,y = 5,7
tes = [[0]*y for _ in range(x)]
for i in range(x):
    for j in range(y):
        tes[i][j] = (i^j) + 1

for i in tes:
    print(i)

n = 5
# m = [1,2,3]
# ab = [[1,5],[2,5],[3,5],[4,5],[1,4],[2,4],[3,4],[2,3]]
ab = [[1,5],[2,5],[3,5],[4,5],[1,4],[2,4],[3,4],[2,3],[1,3],[1,2]]
cd = [[2,5],[3,5],[4,5],[3,4],[1,4]]
ef = [[2,5],[3,5]]

def make_links(xy):
    links = [[] for _ in range(n+1)]
    for x,y in xy:
        links[x-1].append(y-1)
        links[y-1].append(x-1)
    return links

gr = []
for i in range(n):
    gr.append([[0]*n for _ in range(n)])

links_ab = make_links(ab)
links_cd = make_links(cd)
links_ef = make_links(ef)

for i in range(n-1,-1,-1):
    for j in range(n-1,-1,-1):
        for k in range(n-1,-1,-1):
            check = 0
            for l in links_ab[i]:
                if(l > i)&(gr[l][j][k] == 1):
                    check = 1
            if(check==1):
                continue
            for l in links_cd[j]:
                if(l > j)&(gr[i][l][k] == 1):
                    check = 1
            if(check==1):
                continue
            for l in links_ef[k]:
                if(l > k)&(gr[i][j][l] == 1):
                    check = 1
            if(check==1):
                continue
            gr[i][j][k] = 1

for i in range(n):
    for j in range(n):
        print(gr[i][j])
    print('')
