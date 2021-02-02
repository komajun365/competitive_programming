# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
mod = 10**9 + 7

nums = set()
d = {}
for i in range(1,10**6):
    a = n//i
    b = 1 + n//(i+1)
    d[i] = a
    nums.add(i)
    nums.add(a)
    if(i >= b):
        break
    d[b] = i
    nums.add(b)

d = sorted(d.items())

dic_en = {}
dic_de = {}
nums = sorted(list(nums))
cnt = [0] * len(nums)
done = 0
for i,num in enumerate(nums):
    dic_en[num] = i
    dic_de[i] = num
    cnt[i] = num - done
    done = num

d = []
for num in nums:
    d.append((dic_en[num],  dic_en[n//num]))

op = cnt[::]

def update(op):
    n = len(nums)
    res = [0] * (n+1)
    for a,b in d:
        res[0] += op[a]
        res[b+1] -= op[a]
    res[0] %= mod
    for i in range(1,n):
        res[i] += res[i-1]
        res[i] %= mod
    for i in range(n):
        res[i] *= cnt[i]
        res[i] %= mod
    return res[:-1]

for i in range(k-1):
    op = update(op)

ans = sum(op) % mod

print(ans)
