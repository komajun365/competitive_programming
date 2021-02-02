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

x,k,d = map(int,input().split())
max_d = k*d
if( abs(x) < abs(max_d) ):
    tmp = x%d
    min_move = (x-tmp)//d
    if( (k-min_move) % 2 == 0 ):
        ans = tmp
    else:
        ans = abs(d-tmp)
else:
    ans = abs(x) - max_d
print(ans)
