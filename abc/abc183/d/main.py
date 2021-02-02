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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,w,*stp = map(int,read().split())

lim = 2*10**5 + 2
imos = [0] * lim
it = iter(stp)
for s,t,p in zip(it,it,it):
    imos[s] += p
    imos[t] -= p

for i in range(lim):
    imos[i] += imos[i-1]

if(max(imos) <= w):
    print('Yes')
else:
    print('No')
