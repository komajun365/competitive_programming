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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

p = 1000
cnt = [0] * (p+1)

for i in range(1,334):
    i2 = i**2
    for j in range(i,500):
        if 1000 - i - j < j:
            break
        j2 = j**2
        k2 = i2+j2
        k = round(k2**0.5)
        if i + j + k > p:
            continue
        if k**2 == k2:
            cnt[i+j+k] += 1

m = max(cnt)
for i in range(p+1):
    if cnt[i] == m:
        print(i)







