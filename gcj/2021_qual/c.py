# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read

t,*data = map(int,read().split())
def calc(n, c):
    lim = n * (n+1)//2 -1
    if c > lim or c < n-1:
        return 'IMPOSSIBLE'

    c -= n-1
    res = [n]
    for i in range(n-1,0,-1):
        move = min(c, n-i)
        res = res[:move][::-1] + [i] + res[move:]
        c -= move
    return ' '.join(map(str,res))

ans = [''] * t
idx = 0
for i in range(t):
    n = data[idx]
    c = data[idx+1]
    idx += 2
    res = calc(n,c)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))


