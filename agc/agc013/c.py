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

n,l,t,*xw = map(int,read().split())
if(n==1):
    x,w = xw
    sp = 3-w*2
    ans = (x+t*sp)%l
    print(ans)
    exit()

w_ant = [[],[],[]]
for i in range(n):
    x,w = xw[i*2:i*2+2]
    sp = 3-w*2
    w_ant[w].append([i,x, (x+t*sp)%l ])

p_t = w_ant[1] + w_ant[2]
p_t.sort(key=lambda x: x[2])

def calc_who(i,x,w):
    if(w==1):
        touch = 0
        for j,xj,_ in w_ant[2]:
            length = t*2 + l - (xj-x)%l
            touch += length // l
        res = (i + touch)%n
    else:
        touch = 0
        for j,xj,_ in w_ant[1]:
            length = t*2 + l - (x-xj)%l
            touch += length // l
        res = (i - touch)%n
    return res

i0  = p_t[0][0]
i1  = p_t[1][0]
a0 = calc_who(i0,xw[i0*2],xw[i0*2+1])
a1 = calc_who(i1,xw[i1*2],xw[i1*2+1])

if(n==2):
    ans = [0,0]
    ans[a0] = p_t[0][2]
    ans[a1] = p_t[1][2]
    print('\n'.join(map(str,ans)))
    exit()


if(a0 > a1):
    a0,a1 = a1,a0
if(a0==0)&(a1==n-1):
    a0=n-1
    a1=0

if(a0==0):
    ans = [i[2] for i in p_t]
else:
    ans = [i[2] for i in p_t[-a0:]] + [i[2] for i in p_t[:-a0]]
print('\n'.join(map(str,ans)))




'''
蟻の並び順は変わらない。
T秒後に蟻たちのいる位置はすぐわかる。

1の蟻が前進方向にぶつかれるのは2、
2の蟻が前進方向にぶつかれるのは3、・・・

1の蟻が前方向にすり抜け続けるとして、
a匹の蟻とすれ違ったとき、
本当にその場所にいるのは、
1 + a%n番目の蟻である

向かい合わせに進む蟻のうち、
距離2Nですり抜けが発生する。

'''
