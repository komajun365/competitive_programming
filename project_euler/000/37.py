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
cnt = 0
for pi in primes:
    if pi < 10:
        continue

    tmp = 0
    x = 10
    while pi != pi % x:
        if not pi % x in primes:
            break
        x *= 10
    else:
        tmp += 1
    
    x = pi // 10
    while x != 0:
        if not x in primes:
            break
        x //= 10
    else:
        tmp += 1
    
    if tmp == 2:
        ans += pi
        cnt += 1
        print(pi)



print(ans)
print(cnt)

'''
とりあえず篩。


'''
