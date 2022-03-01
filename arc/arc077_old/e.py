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

ex = [0] * m
left = [0] * (2*m)
right = [[0,0] for _ in range(2*m)]

ans = 0
for i in range(n-1):
    a0 = a[i]-1
    a1 = a[i+1]-1
    ans += (a1-a0)%m
    left[a0+1] += 1
    right[a1 + (a0>a1)*m][0] += 1
    right[a1 + (a0>a1)*m][1] += (a1-a0)%m -1

now = left[0]
dif = 0
for i in range(1,2*m):
    dif += now
    ex[i%m] -= dif
    now += left[i] - right[i][0]
    dif -= right[i][1]

ans += min(ex)
print(ans)

# print(left)
# print(right)
# print(ex)



'''
a->b のとき
・(x-a)%m < (b-a)%m
1 + (b-x)%m
= (b-x+1)%m

・(x-a)%m >= (b-a)%m
(b-a)%m



2-5

0,1,2,3,4,5,6,7
3,3,3,3,2,1,3,3

0,0,0,0,-1,-2,0,0

4-3
0,1,2,3,4,5,6,7
4,3,2,1,7,7,6,5
'''
