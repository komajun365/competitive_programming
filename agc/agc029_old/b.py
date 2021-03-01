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

from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
a2 = list(set(a))
a2.sort(reverse=True)

d = defaultdict(int)
for i in a:
    d[i] += 1

ans = 0
for i in a2:
    next = 2**(i-1).bit_length()
    if(i==next):
        ans += d[i]//2
    else:
        pair = min(d[i],d[next-i])
        d[next-i] -= pair
        ans += pair
print(ans)




'''
最大マッチングやんけ！
・・・と思ったけど、その考えで行くと辺の数がやばい

大きい奴からペアにしていっていいと思う。

'''
