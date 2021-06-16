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
cp = data[:2*n]
q = data[2*n]
lr = data[2*n+1:]

cs = [[0] * (n+1) for _ in range(2)]

for i in range(n):
    c,p = cp[i*2:i*2+2]
    c -= 1
    for j in range(2):
        cs[j][i] = cs[j][i-1]
    cs[c][i] += p

ans = []
it = iter(lr)
for l,r in zip(it,it):
    r -= 1
    l -= 2
    tmp = [0,0]
    for i in range(2):
        tmp[i] = cs[i][r] - cs[i][l]
    ans.append('{} {}'.format(*tmp))

print('\n'.join(ans))


