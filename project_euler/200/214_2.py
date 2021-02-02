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

'''
素数列挙＆再帰関数でいけるかしら

φ(n)の求め方
素因数分解して、
a**x * b**y * c**z
φ(n) = (a**(x-1)-(a-1))*(b**(y-1)*(b-1))*(c**z-z)
 = n*(a-1)*(b-1)*(c-1)//(a*b*c)

素因数がわかれば計算できる！
とはいえ、最大でO(10*5)くらいはありそうですけれども・・・
ひとまずやってみましょう。

=====

きつかったです。
下からφ(x)を作っていきましょう。

φ(x)=yだっととします。
φ(2x)=y'は？
・x%2==0の場合
y' = 2y
・x%2==1の場合
y' = y

φ(3x)=y'は？
・x%3==0の場合
y' = 3y
・x%3!=0の場合
y' = 2y

'''
n = 4*10**7
# n = 10**4
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

primes = sieve(n)

phi = [0] * (n+1)
phi[1] = 1

def calc_phi(x):
    if(phi[x] != 0):
        return phi[x]

    for i in primes:
        if(i**2 > x):
            phi[x] = x-1
            return x-1
        if(x%i==0):
            if(x%(i*i)!=0):
                phi[x] = calc_phi(x//i) * (i-1)
            else:
                phi[x] = calc_phi(x//i) * i
            return phi[x]
    return None

phi_len = [0] * (n+1)
phi_len[1] = 1
for i in range(2,n+1):
    if(i%(10**6)==0):
        print(i)
    phi_len[i] = 1 + phi_len[calc_phi(i)]

ans = 0
for i in primes:
    if(phi_len[i] == 25):
        ans += i

print(ans)



# for i in range(2,100+1):
#     for j in primes:
#         if(j**2 > i):
#             phi[i] = i-1
#             break
#         if(i%j==0):
#             if(i%(j**2)==0):
#                 phi[i] = phi[i//j] * j
#             else:
#                 phi[i] = phi[i//j] * (j-1)
#             break
#
# print(phi[:20])
#
# for i in primes:
#     done_list = sorted(list(done))
#     for j in done_list:
#         if(j==1):
#             p = i-1
#         else:
#             p = phi[j] * i
#         j = j*i
#         if(j>n):
#             print(i)
#             break
#         while(j<=n):
#             done.add(j)
#             phi[j] = p
#             j *= i
#             p *= i
#
# phi_length = [0]*(n+1)
# phi_length[1] = 1
# for i in range(2,n+1):
#     if(i%(10**6)==0):
#         print(i)
#     phi_length[i] = phi_length[phi[i]] + 1
#
# ans = 0
# for i in primes:
#     if(phi_length[i] == 25):
#         ans += i
#         # print(i)
#
# print(ans)
