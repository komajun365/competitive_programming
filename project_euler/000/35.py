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
f = open('p018_triangle.txt', 'r')
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

n = 10**6
primes = set(sieve(n))

ans = 0
hoge = 0
for pi in primes:
    hoge += 1
    for x in range(1,7):
        if 10**x > pi:
            cnt = 0
            for _ in range(x):
                if pi in primes:
                    cnt += 1
                head = pi // 10**(x-1)
                pi = (pi * 10) % 10**x + head
            if cnt == x:
                ans += 1
                print(pi)
            break

print(ans)
print(hoge)

'''
とりあえず篩。
偶数使ってたらアウトだけど、あんまり考えなくてもよさそう。

'''
