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

x,y = map(int,input().split('/'))
cand = x*2//y

ans = []
for i in range(cand,cand+3):
    ym2 = y*i*(i+1) - 2*i*x
    if(ym2%(2*y)==0):
        num = ym2//(2*y)
        if(1 <= num <= i):
            ans.append((i,num))

if(len(ans)==0):
    print('Impossible')
else:
    for i in ans:
        print(' '.join(map(str,i)))



'''

X/Yは

(n(n+1)-n)/2n ~ (n(n+1)-1)/2n

(n+2)

(n(n+1)-2m)/2n = x/y
n(n+1)-2m = 2nx/y
yn(n+1)-2ym=2nx
2ym = yn(n+1)-2nx



'''

# for i in range(1,30):
#     left = (i*(i+1)-2*i)/(2*i)
#     right = (i*(i+1)-2)/(2*i)
#     print(i,left,right)


# n = 9999
# m = 4999
# tmp = (n*(n+1)//2 - m)/n
# print(tmp)
