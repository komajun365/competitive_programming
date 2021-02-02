import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
mod = 10**9 + 7

ans = 0
lim = 2*(10**5) + 5
mothers = [1] * lim
mothers_inv = [1] * lim
for i in range(1, lim):
    mothers[i] = mothers[i-1] * i % mod
    mothers_inv[i] = pow(mothers[i], mod-2, mod)


def calc(n,k):
    child = mothers[n] * mothers_inv[n-k] % mod
    mother_inv = mothers_inv[k]
    return((child * mother_inv)%mod)

def calc2(n,k):
    child = 1
    for i in range(n, n-k, -1):
        child = child * i % mod
    mother_inv = mothers_inv[k]
    return((child * mother_inv)%mod)

if( n <= k+1):
    ans = calc2(2*n-1, n-1)
    print(ans)
    exit()

ans = calc2(2*n-1, n-1)

for i in range(1,n-k):
    if(i ==1):
        c1 = 1
    else:
        c1 = calc(n-1, i-1)

    c2 = calc(n, i)
    ans = (ans - c1 * c2)%mod


print(ans)
