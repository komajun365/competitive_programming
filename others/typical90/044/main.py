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
txy = data[n:]

shift = 0
ans = []
it = iter(txy)
for t,x,y in zip(it,it,it):
    if t == 1:
        x = (x - 1 + shift) % n
        y = (y - 1 + shift) % n
        a[x],a[y] = a[y],a[x]
    elif t == 2:
        shift -= 1
    else:
        x = (x - 1 + shift) % n
        ans.append(a[x])
print('\n'.join(map(str,ans)))

