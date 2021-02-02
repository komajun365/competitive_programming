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

# ヒープキュー（最小値・最大値の取得）
from heapq import heappop,heappush

import sys
read = sys.stdin.buffer.read
x,y,z,*abc = map(int,read().split())
n = x+y+z

def encode(cost,person):
    return (cost << 20) + person

hqs = []
for i in range(3):
    hqs.append([[] for _ in range(3)])

ans = 0
for i in range(n):
    a,b,c = abc[i*3:i*3+3]
    max_num = max(a,b,c)
    ans += max_num
    heappush(hqs[0][0], encode(max_num - a ,i))
    heappush(hqs[1][1], encode(max_num - b ,i))
    heappush(hqs[2][2], encode(max_num - c ,i))

var = [-1] * n
rem = [x,y,z]
inf = 10**10

for _ in range(n):
    cost = inf
    query = []
    for i in range(3):
        while(hqs[i][i]):
            num = hqs[i][i][0]
            c,p = divmod(num, 1<<20)
            if var[p] != -1:
                heappop(hqs[i][i])
            else:
                break
        else:
            continue
        if rem[i] != 0:            
            if cost > c:
                cost = c
                query = [[p,i,i]]
        elif sum(rem) == max(rem):
            j = -1
            for k in range(3):
                if rem[k] > 0:
                    j = k
                    break
            k = 3 - i - j
            while(hqs[i][j]):
                num_j = hqs[i][j][0]
                cj,pj = divmod(num_j, 1<<20)
                if var[pj] != i:
                    heappop(hqs[i][j])
                else:
                    break
            else:
                continue
            if cost > c+cj:
                    cost = c+cj
                    query = [[p,i,i], [pj,i,j]]

            while(hqs[i][k]):
                num_k = hqs[i][k][0]
                ck,pk = divmod(num_k, 1<<20)
                if var[pk] != i:
                    heappop(hqs[i][k])
                else:
                    break
            else:
                continue
            while(hqs[k][j]):
                num_j = hqs[k][j][0]
                cj,pj = divmod(num_j, 1<<20)
                if var[pj] != k:
                    heappop(hqs[k][j])
                else:
                    break
            else:
                continue
            if cost > c+cj+ck:
                cost = c+cj+ck
                query = [[p,i,i], [pk,i,k],[pj,k,j]]

            
        else:
            for j in range(3):
                # print(_,i,j)
                if i == j or rem[j] == 0:
                    continue
                while(hqs[i][j]):
                    num_j = hqs[i][j][0]
                    cj,pj = divmod(num_j, 1<<20)
                    if var[pj] != i:
                        heappop(hqs[i][j])
                    else:
                        break
                else:
                    continue
                # print(_,i,j)
                if cost > c+cj:
                    cost = c+cj
                    query = [[p,i,i], [pj,i,j]]
    
    ans -= cost
    for p,i,j in query:
        if i == j:
            rem[i] -= 1
            var[p] = i
            heappop(hqs[i][i])
            for k in range(3):
                if i == k:
                    continue
                ci = abc[3*p + i]
                ck = abc[3*p + k]
                heappush( hqs[i][k], encode(ci-ck, p) )
        else:
            rem[i] += 1
            rem[j] -= 1
            var[p] = j
            heappop(hqs[i][j])
            for k in range(3):
                if i == k:
                    continue
                ci = abc[3*p + i]
                ck = abc[3*p + k]
                heappush( hqs[i][k], encode(ci-ck, p) )
    
    # print(cost)
    # print(query)
    # print(ans)
    # print('rem',rem)
    # print(hqs)

print(ans)





