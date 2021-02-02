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

primes = set(sieve(10**6))

# for i in range(1000):
#     if((i+1)**3 - i**3 >= 10**6):
#         print(i+1,i)
#         print((i+1)**3,(i)**3)
#         break

ans = 0
for i in range(1,600):
    for j in range(i+1,600):
        num = j**3-i**3
        if(num > 10**6):
            break
        if(num in primes):
            ans += 1

print(ans)

'''
n^3+pn^2 = (n+p) * n^2

pが素数なので、n+pとnは素
n+p,n どっちも立方数のときにしかできないということがわかる。

n = k^3
n+p = l^3
として、k,lを探索すればよい。

l^3 - k^3 = (l-y)(l^2+lk+k^2)
(1,1) - (1,101)
(1000,1001) -> 3003001

探索範囲はo(10**6)以下
→　確認してみるとk=578未満でOK

'''
