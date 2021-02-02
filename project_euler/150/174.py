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

n = 10**6
cnt = [0] * (n+1)

for k in range(1,n):
    if(4*k*(k+1) > n):
        break
    for y in range(1,n):
        t = 4*k*(k+y)
        if(t > n):
            break
        cnt[t] += 1

ans = 0
for i in range(1,11):
    ans += cnt.count(i)

print(ans)
print(cnt[:11])


'''
t = x^2 - y^2 ( ただしx-yは2以上の偶数)

x^2-y^2 = (x+y)(x-y)
x-y = 2k として
 = 4k(k+y)

n=10**6
O(nlogn)で数え上げ

'''
