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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

r,c,n = map(int,readline().split())
data = list(map(int,read().split()))
p = []
for i in range(n):
    x1,y1,x2,y2 = data[i*4:i*4+4]
    if((x1==0)|(x1==r)|(y1==0)|(y1==c))&((x2==0)|(x2==r)|(y2==0)|(y2==c)):
        for x,y in zip([x1,x2],[y1,y2]):
            num = 0
            if(x==0):
                num = y
            elif(x==r):
                num = r+2*c-y
            elif(y==0):
                num = 2*(r+c)-x
            else:
                num = c+x
            p.append([num,i])

p.sort()
d = []
for _,i in p:
    if(not d):
        d.append(i)
    else:
        right = d.pop()
        if(right != i):
            d.append(right)
            d.append(i)

if(len(d)==0):
    print('YES')
else:
    print('NO')


# p_len = len(p)
# for i in range(p_len):
#     left = (i-1)%p_len
#     right = (i+1)%p_len
#
#     if(p[i][1] != p[left][1])&(p[i][1] != p[right][1]):
#         print('NO')
#         exit()
#
# print('YES')


'''
盤面の境界上を結ぶと分断される。
それだけを考えればよい。

反時計回りで原点からの距離を取ってみよう

'''
