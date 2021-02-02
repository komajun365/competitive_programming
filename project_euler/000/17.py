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


len1_19 = [0,3,3,5,4,4,3,5,5,4,
            3,6,6,8,8,7,7,9,8,8]
len20_90 = [0,0,6,6,5,5,5,7,6,6]
len100 = 7

ans = 0
for i in range(1,1000):
    if(i >= 100):
        ans += len100
        if(i%100!=0):
            ans += 3
        ans += len1_19[i//100]

    i %= 100
    if(i >= 20):
        ans += len20_90[i//10]
        ans += len1_19[i%10]
    else:
        ans += len1_19[i]

ans += 11
print(ans)
