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

n,q,*data = map(int,read().split())
a = data[:n]
lrv = data[n:]

tot = 0
dif = []
for i in range(n-1):
    dif.append(a[i+1]-a[i])
    tot += abs(dif[-1])

ans = []
it = iter(lrv)
for l,r,v in zip(it,it,it):
    l -= 1
    r -= 1
    if l != 0:
        di = dif[l-1] + v
        tot += abs(di) - abs(dif[l-1])
        dif[l-1] = di
    if r != n-1:
        di = dif[r] - v
        tot += abs(di) - abs(dif[r])
        dif[r] = di
    ans.append(tot)
    # print(dif)
print('\n'.join(map(str,ans)))


