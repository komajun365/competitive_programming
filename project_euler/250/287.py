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

from functools import lru_cache

n = 20
x_n_1 = 2**(n-1)
x_2n_2 = 2**(2*n-2)
exp = [0] * (2**(n-1) + 1)
for i in range(2**(n-1) + 1):
    exp[i] = i**2

@lru_cache(maxsize=None)
def calc_mm(x0,x1):
    x0 -= x_n_1
    x1 -= (1+x_n_1)
    if(x0<=0<=x1):
        x_min = 0
        x_max = exp[max(-x0,x1)]
    else:
        x_min = exp[min( abs(x0), abs(x1))]
        x_max = exp[max( abs(x0), abs(x1))]
    return x_min,x_max

@lru_cache(maxsize=None)
def calc_len(x0,y0,n):
    x1 = x0+n
    y1 = y0+n

    if( n == 1):
        # print(11)
        return 2
    x_min,x_max = calc_mm(x0,x1)
    y_min,y_max = calc_mm(y0,y1)
    # print(x0,x1,y0,y1)
    # print(':',x_min,x_max,y_min,y_max)
    if(x_min+y_min <= x_2n_2 < x_max+y_max):
        if(n==2):
            return 9
        # print(0)
        n2 = n//2
        tmp = (calc_len2(x0,y0,n2)
                + calc_len2(x0,y0+n2,n2)
                 + calc_len2(x0+n2,y0,n2)
                 + calc_len2(x0+n2,y0+n2,n2))
        return tmp + 1
    else:
        # print(11)
        return 2

def calc_len2(x0,y0,n):
    x0,y0 = min(x0,y0),max(x0,y0)
    return calc_len(x0,y0,n)



print(calc_len2(0,0,2**n))


'''
■□

D2
□■■■
■■■■
□■■■
□□■□

0 0 11101010 10 0 11101111 0 10101011

D3
9,4,1,0,1,4,9,16

□□■■■■■□
□■■■■■■■
□■■■■■■■
■■■■■■■■
□■■■■■■■
□■■■■■■■
□□■■■■■□
□□□□■□□□

0 0000
9+2+9+2 2+9+2+2
9+2+9+2 9+2+9+2

領域の中で最大、最小値を計算して、
全部白or全部黒がわかれば書き込んでいく、感じでいけないかしら。
BFSみたいな感じ。

'''
