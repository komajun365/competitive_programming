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

import random
import itertools

n,k = 7,3
a = [random.randint(-3, 3) for i in range(5)]
print(a)
# a = [-8, 5, 7, -3, 3]

t_ans = -10**10
for i in itertools.permutations(a, k):
    tmp = 1
    for j in i:
        tmp *= j
    t_ans = max(t_ans,tmp)

print(t_ans)

# n,k = map(int,input().split())
# a = list(map(int,input().split()))
mod = 10**9 +7

a_plus = []
a_minus = []
cnt_0 = 0

for ai in a:
    if(ai==0):
        cnt_0 += 1
    elif(ai > 0):
        a_plus.append(ai)
    else:
        a_minus.append(ai)

a_plus.sort(reverse = True)
a_minus.sort()

cnt_p = len(a_plus)
cnt_m = len(a_minus)

if(cnt_p + cnt_m < k):
    print(0)
    exit()


if(cnt_m == n)&(k%2==1):
    ans = 1
    for i in range(k):
        ans *= a_minus[cnt_m - 1 - i]
        ans %= mod
    print(ans)
    exit()

if(cnt_p == 0)&(k%2==1):
    print(0)
    exit()

p_ind = 0
m_ind = 0

ans = 1
if(k%2==1):
    last_p = a_plus[0]
    cnt_p -= 1
    a_plus = a_plus[1:]

for i in range(k//2):
    tmp_p = 0
    tmp_m = 0
    if(p_ind + 2 <= cnt_p ):
        tmp_p = a_plus[p_ind] * a_plus[p_ind+1]

    if(m_ind + 2 <= cnt_m ):
        tmp_m = a_minus[m_ind] * a_minus[m_ind+1]

    if(tmp_p > tmp_m):
        ans *= tmp_p
        p_ind += 2
    else:
        ans *= tmp_m
        m_ind += 2
    ans %= mod

if(k%2==1):
    ans *= last_p

ans %= mod
print(ans)
print(a_plus)
print(a_minus)
print(p_ind,m_ind)
print(cnt_p)
