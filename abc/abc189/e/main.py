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
n,*data = map(int,read().split())
xy = data[:2*n]
m = data[2*n]
op = []

idx = 2*n+1
for _ in range(m):
    if data[idx] < 3:
        op.append([data[idx]])
        idx += 1
    else:
        op.append(data[idx:idx+2])
        idx += 2

q = data[idx]
ab = data[idx+1:]

ab2 = []
for i in range(q):
    ab2.append([i,ab[i*2],ab[i*2+1]-1])
ab2.sort(key = lambda x:x[1]*-1)

ans = [[0,0] for _ in range(q)]

xi = [1,0,0]
yi = [0,1,0]

for i in range(m+1):
    while(ab2):
        if ab2[-1][1] == i:
            idx,a,b = ab2.pop()
            ans[idx][0] = xi[0] * xy[2*b] + xi[1] * xy[2*b+1] + xi[2]
            ans[idx][1] = yi[0] * xy[2*b] + yi[1] * xy[2*b+1] + yi[2]
        else:
            break
    
    if i == m:
        break
    
    opi = op[i]
    if opi[0] == 1:
        xj = yi[::]
        yj = [ xi[0]*-1, xi[1]*-1, xi[2] * -1 ]
    elif opi[0] == 2:
        xj = [ yi[0]*-1, yi[1]*-1, yi[2] * -1 ]
        yj = xi[::]
    elif opi[0] == 3:
        xj = [ xi[0]*-1, xi[1]*-1, xi[2] * -1 + 2*opi[1] ]
        yj = yi[::]
    else:
        xj = xi[::]
        yj = [ yi[0]*-1, yi[1]*-1, yi[2] * -1 + 2*opi[1] ]
    xi,xj = xj,xi
    yi,yj = yj,yi

print('\n'.join(map(lambda x: ' '.join(map(str,x)),ans)))


