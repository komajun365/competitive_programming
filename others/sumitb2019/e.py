import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
a = list(map(int, input().split()))

MOD = 1000000007

dic = {}
dic[0] = 3
for i in range(1,n+1):
    dic[i] = 0

ans = 1
for i in range(n):
    ans = ans * dic[a[i]] % MOD
    dic[a[i]] -= 1
    dic[a[i] + 1] += 1

print(ans)
