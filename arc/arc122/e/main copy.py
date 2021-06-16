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

links = [[] for _ in range(n)]
deg_in = [0] * n
for i in range(n-1):
    for j in range(i+1,n):
        if a[j] % a[i] == 0:
            links[i].append(j)
            deg_in[j] += 1

print(links)

for i in range(n):
    lcm = 1
    for j in links[i]:
        lcm = lcm * a[j] // gcd(lcm,a[j])
    if lcm % a[i] == 0:
        print('No')
        exit()

ans = []
stack = []
for i in range(n):
    if deg_in[i] == 0:
        stack.append(i)

while stack:
    i = stack.pop()
    ans.append(a[i])
    for j in links[i]:
        deg_in[j] -= 1
        if deg_in[j] == 0:
            stack.append(j)

print('Yes')
print(' '.join(map(str,ans)))

def check(ans):
    lcm = 1
    for ai in ans:
        lcm2 = lcm * ai // gcd(lcm,ai)
    if lcm2 <= lcm:
        print('NG')
        exit()
    lcm,lcm2 = lcm2,lcm




# def sieve(n):
#     if( n <= 1):
#         return []
#     elif(n==2):
#         return [2]

#     primes = [2]
#     len_list = (n+1)//2
#     len_sqrt = int(len_list**0.5) + 1
#     flags = [True] * len_list
#     flags[0] = False
#     for i in range(len_sqrt):
#         if(flags[i]):
#             start = ((i*2+1)**2)//2
#             for j in range( start, len_list, i*2+1):
#                 flags[j] = False
#     return [2] + [i*2+1 for i in range(len_list) if flags[i]]

# primes = sieve(100)

# now = 1
# for i in primes:
#     now *= i
#     print(i,now)
#     if now > 10**18:
#         break