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

n,m = map(int,input().split())
mod = 10**9+7
n2 = abs(n)

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+1 ):
        if(temp%i == 0):
            count=0
            while( temp%i == 0):
                count += 1
                temp = temp // i
            arr.append([i, count])

    if(temp != 1):
        arr.append([temp, 1])

    if(arr == []):
        arr.append([n, 1])

    return arr

max = 10**5 + 1000
fac, finv, inv = [0]*max, [0]*max, [0]*max

def comInit(max):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max)

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

ans0 = 1
arr = factorization(n2)

for _,i in arr:
    ans0 *= com(i+m-1,i)
    ans0 %= mod

ans = 0
for i in range(m+1):
    if(n>0)&(i%2==1):
        continue
    if(n<0)&(i%2==0):
        continue

    ans += ans0 * com(m,i)
    ans %= mod

print(ans)



'''
素因数に分解してあーだこーだ。


'''
