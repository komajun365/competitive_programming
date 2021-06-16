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

n,m,*data = map(int,read().split())
ab = data[:2*m]
q = data[2*m]
tx = data[2*m+1:]

links = [[] for _ in range(n)]
deg = [0] * n
it = iter(ab)
for a,b in zip(it,it):
    a -= 1
    b -= 1
    links[a].append(b)
    links[b].append(a)
    deg[a] += 1
    deg[b] += 1

sb = [[] for _ in range(n)]
for i in range(n):
    small = []
    big = []
    for j in links[i]:
        if deg[i] > deg[j]:
            small.append(j)
        elif deg[i] < deg[j]:
            big.append(j)
        else:
            if i < j:
                big.append(j)
            else:
                small.append(j)
    sb[i].append(small[::])
    sb[i].append(big[::])

ans = []
take_m = [0] * n
get_m = [0] * n
check = [dict() for _ in range(n)]

it = iter(tx)
for t,x in zip(it,it):
    x -= 1
    if t == 1:
        take_m[x] += 1
        for j in sb[x][1]:
            get_m[j] += 1
    else:
        tmp = get_m[x]
        get_m[x] = 0
        for j in sb[x][1]:
            tmp += take_m[j] - check[x].get(j,0)
            check[x][j] = take_m[j]
        ans.append(tmp)
    # print(take_m)
    # print(get_m)
    # print(check)

print('\n'.join(map(str,ans)))





