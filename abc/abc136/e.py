import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
a = list(map(int, input().split()))

# 約数リスト
def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors

sum_a = sum(a)
divisors = sorted(make_divisors(sum_a), reverse=True)

for div in divisors:
    if(sum_a % div != 0):
        continue

    mod_a = []
    for ai in a:
        mod_a.append(ai % div)
    mod_a = sorted(mod_a)

    sum_mod_a = sum(mod_a)
    k_min = sum(mod_a[: (n-sum_mod_a//div) ])

    if(k_min <= k):
        print(div)
        exit()

# 絶対1で割り切れるからここにはこないけど。。。
print(-1)
