# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

from math import gcd

n = int(input())
a = list(map(int,input().split()))
mod = 998244353

a.sort()

ans = a[0]
ans %= mod

for i in range(1,n):
    ans *= gcd(a[i],i)
    ans %= mod

print(ans)

# a.sort()
# gcd_num = a[0]

# for ai in a:
#     gcd_num = gcd(gcd_num, ai)

# a = [ai//gcd_num for ai in a]

# ans = pow(gcd_num, n, mod)
# ans *= a[0]
# ans %= mod

# for i in range(1,n):
#     if a[i] % i == 0:
#         ans *= i
#         ans %= mod

# print(ans)

'''
3,3,3,3

6a=18
6ab+3ac+2ad=99
3abc+2abd+acd=216
abcd=81

11,11,11,11
6a=66
6ab+3ac+2ad=121
3abc+2abd+acd=216
abcd=81


24a
24ab+12ac+8ad+6ae
12abc+8abd+



'''