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

import copy

p_min = 10**14
width = 3300000
mod = 1234567891011

def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    len_list = (n+1)//2
    len_sqrt = int(len_list**0.5) + 1
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_sqrt):
        if(flags[i]):
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return [2] + [i*2+1 for i in range(len_list) if flags[i]]

# left　<=　p　<　right な素数のリスト
def sieve_range(left,right):
    n = 100 + int(right**0.5)
    primes_base = sieve(n)

    if( len(primes_base)==0):
        return []

    primes = []
    left += (left%2 == 0)
    len_list = (right-left)//2 + 1
    flags = [True] * len_list
    for i in primes_base[1:]:
        dif = (i - (left % i))%i
        if(dif%2 == 1):
            dif += i
        start = dif//2
        for j in range( start, len_list, i):
            flags[j] = False
    return [i*2+left for i in range(len_list) if flags[i]]

a = sieve_range(p_min,p_min+width)

print(len(a))
print(a[:10])
print(a[-10:])

def calc_product(a,b):
    #n*nの行列が与えられるとする。
    n = len(a)
    mod = 1234567891011

    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j] %= mod

    return res

exp_max = 50
exp_fib = [[] for _ in range(exp_max)]
exp_fib[0] = [[1,1],[1,0]]
for i in range(1,exp_max):
    exp_fib[i] = copy.deepcopy(calc_product(exp_fib[i-1],exp_fib[i-1]))

ans = 0
for cnt,i in enumerate(a[:100000]):
    if(cnt%5000==0):
        print(cnt)
    mat = [[1,0],[0,1]]
    x = 0
    while(i>0):
        if(i&1):
            mat = copy.deepcopy(calc_product(mat,exp_fib[x]))
        i //= 2
        x += 1

    ans += mat[0][1]
    ans %= mod

# for i in range(10):
#     mat = [[1,0],[0,1]]
#     x = 0
#     while(i>0):
#         if(i&1):
#             mat = copy.deepcopy(calc_product(mat,exp_fib[x]))
#         i //= 2
#         x += 1
#
#     ans += mat[0][1]
#     ans %= mod
#     print(mat[0][1],ans)

print(ans)



'''
a(n)は篩の変形で処理する。

フィボナッチの項は行列累乗で行きましょう。
a(100000)がだいたい10**14 + 3*10**5 くらいなので、
|1 1|
|1 0|
これの2**50くらいまで求めておけばlogのオーダーで計算できそうです。

|2 1|
|1 1|

|5 3|
|3 2|

|34 21|
|21 13|

'''
