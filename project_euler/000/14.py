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


# 再帰関数の上限解除
import sys
print(sys.getrecursionlimit())

# sys.setrecursionlimit(10**6)
from collections import defaultdict
d = defaultdict(lambda:-1)
d[1] = 1

def calc(x):
    if(d[x]!=-1):
        return d[x]
    if(x%2==0):
        y=x//2
    else:
        y=x*3+1
    d[x] = calc(y) + 1
    return d[x]

ans = 0
max_num = 0
for i in range(1,10**6):
    i_num = calc(i)
    if(max_num < i_num):
        max_num = i_num
        ans = i

print(max_num)
print(ans)
