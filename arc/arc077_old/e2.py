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


n,m = map(int,input().split())
a = list(map(int,input().split()))

imos = [0] * (2*m+2)
ans = 0
for i in range(n-1):
    a0 = a[i]-1
    a1 = a[i+1]-1
    dif = (a1-a0)%m
    ans += dif
    if(dif>=2):
        imos[a0+2] += 1
        imos[a0+dif+1] -= dif
        imos[a0+dif+2] += dif-1

# print(imos)

for i in range(1,2*m+2):
    imos[i] += imos[i-1]
# print(imos)

for i in range(1,2*m+2):
    imos[i] += imos[i-1]
# print(imos)

for i in range(m):
    imos[i] += imos[i+m]

ans -= max(imos[:m])
print(ans)

'''
a->b のとき
・(x-a)%m < (b-a)%m
1 + (b-x)%m
= (b-x+1)%m

・(x-a)%m >= (b-a)%m
(b-a)%m


2-3

0,1,2,3,4,5,6,7
1,1,1,1,1,1,1,1


2-5

0,1,2,3,4,5,6,7
3,3,3,3,2,1,3,3

0,0,0,0,-1,-2,0,0

4-3
0,1,2,3,4,5,6,7
4,3,2,1,7,7,6,5
'''

'''
2回imosをやると、
階差数列を作ることができるテクニック。
'''
