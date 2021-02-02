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
from heapq import heappop,heappush

n,*data = map(int,read().split())
a = data[:n]
b = data[n:n*2]
p = [pi-1 for pi in data[n*2:]]
bag = [[-1,-1] for _ in range(n)] # num,weight

hq = []
coef = 10**10

for i in range(n):
    pi = p[i]
    bag[i][0] = pi
    bag[i][1] = b[pi]
    if i == pi:
        continue
    if b[pi] >= a[i]:
        print(-1)
        exit()
    else:
        heappush(hq, -(b[pi]*coef + i))

ans = 0
op = []
done = [0] * n
while(hq):
    x = heappop(hq) * -1
    i = x % coef
    j = bag[i][0]
    wi = x // coef
    if done[i] == 1:
        continue

    ans += 1
    op.append('{} {}'.format(i+1,j+1))
    done[j] = 1

    wj = bag[j][1]
    p = bag[j][0]
    if p == i:
        done[i] = 1
        continue

    bag[i][0] = p
    bag[i][1] = wj

    heappush(hq, -(wj*coef+i))

print(ans)
if ans != 0:
    print('\n'.join(op))






