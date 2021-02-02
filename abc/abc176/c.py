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

n= input()
a = list(map(int,input().split()))

ans = 0
max_num = a[0]
for ai in a[1:]:
    if(max_num < ai ):
        max_num = ai
    else:
        ans += max_num -ai
print(ans)
