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

n = int(readline())
al = list(map(int,read().split()))
b = al.pop()

ex10 = [0] * 51
ex10[0] = 10%b
for i in range(1,51):
    ex10[i] = (ex10[i-1]*ex10[i-1])%b

def get_ex10(x):
    #10**xを返す
    res = 1
    i = 0
    while(x > 0):
        if(x&1):
            res *= ex10[i]
            res %= b
        x //= 2
        i += 1
    return res

ex = [[0] * (35) for _ in range(11)]
for i in range(1,11):
    ex[i][0] = 1%b
    for j in range(1,35):
        ex[i][j] = ex[i][j-1] + ex[i][j-1]*get_ex10( i*2**(j-1) )
        ex[i][j] %= b

def get_ex(x,y):
    #xをy回繰り返したものを返す
    res = 0
    x_len = len(str(x))
    k = 0
    i = 0
    while(y>0):
        if(y&1):
            res += ex[x_len][i] * get_ex10(k)
            res %= b
            k += x_len*(2**i)
        i += 1
        y //= 2
    return (res*x)%b

ans = 0
keta = 0
it = iter(al[::-1])
for l,a in zip(it,it):
    a_len = len(str(a))
    ans += get_ex(a,l) * get_ex10(keta)
    ans %= b
    keta += a_len * l

print(ans)
