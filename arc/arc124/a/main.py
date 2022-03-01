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
read = sys.stdin.read


n,k,*ck = read().split()
n = int(n)
k = int(k)
mod = 998244353
if k > n:
    print(0)
    exit()

# num = [-1] * n
lr = [-1] * n # L=0,R=1
use = 0
for i in range(k):
    ci,ki = ck[i*2:i*2+2]
    ki = int(ki) - 1
    if lr[ki] != -1:
        print(0)
        exit() 
    if ci == 'L':
        lr[ki] = 0
    else:
        lr[ki] = 1
        use += 1

ans = 1
for i in range(n):
    if lr[i] == 0:
        use += 1
    elif lr[i] == 1:
        use -= 1
    else:
        ans *= use
        ans %= mod
print(ans)



