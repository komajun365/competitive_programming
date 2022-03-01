# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read
import bisect

n,m,q,*data = map(int,read().split())
abst = data[:m*4]
xyz = data[m*4:]

bus = []
for i in range(m):
    a,b,s,t = abst[i*4:i*4+4]
    a -= 1
    b -= 1
    bus.append([s,t,a,b])
bus.sort()

city = [[] for _ in range(n)]
for i in range(m):
    s,t,a,b = bus[i]
    city[a].append([s,i])

city_t = [[] for _ in range(n)]
city_b = [[] for _ in range(n)]
for i in range(n):
    city[i].sort()
    for ti,bi in city[i]:
        city_t[i].append(ti)
        city_b[i].append(bi)

use = [-1] * m
route = []
route2 = []
idx = -1
for i in range(m):
    if use[i] != -1:
        continue

    route.append([])
    route2.append([])
    idx += 1
    now = i
    while True:
        use[now] = idx
        s,t,a,b = bus[now]
        route[-1].append(s)
        route[-1].append(t)
        route2[-1].append(a)
        route2[-1].append(b)

        cand = bisect.bisect_left(city_t[b], t)
        if cand == len(city_t[b]):
            break

        now = city_b[b][cand]

ans = []
it = iter(xyz)
for x,y,z in zip(it,it,it):
    y -= 1
    cand = bisect.bisect_left(city_t[y], x)
    if cand == len(city_t[y]):
        ans.append(str(y+1))
        continue

    bi = city_b[y][cand]
    if bus[bi][0] >= z:
        ans.append(str(y+1))
        continue
    ri = use[bi]
    cand2 = bisect.bisect_left(route[ri], z)
    if cand2 == len(route[ri]):
        ans.append(str(route2[ri][-1] + 1))
        continue

    if cand2 % 2 == 0:
        ans.append(str(route2[ri][cand2] + 1))
        continue
    else:
        c1 = route2[ri][cand2-1] + 1
        c2 = route2[ri][cand2] + 1
        ans.append('{} {}'.format(c1,c2))
        continue

print('\n'.join(ans))



# print(use)
# print(route)




# print(city)
# print(bus)
# print(city_t)
# print(city_b)


