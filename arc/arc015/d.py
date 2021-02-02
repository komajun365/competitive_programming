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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

T,n,p = readline().split()
T = int(T)
n = int(n)
p = float(p)
qxt = read().split()

rate = [0] * (T+2)
rate[0] = 1
rate[-1] = -1

it = iter(qxt)
for q,x,t in zip(it,it,it):
    q = float(q)
    x = int(x)
    t = int(t)
    ex = p*q*(x-1)
    rate[1] += ex
    rate[min(1+t,T+1)] -= ex

for i in range(1,T+2):
    rate[i] += rate[i-1]

ans = 0
now = 1
for i in range(T):
    now *= rate[i]
    ans += now


print('{:.10f}'.format(ans))
# print(ans)
# print('{:.120f}'.format(0.1**100))



'''
x秒前の効果による倍率の期待値は独立、
ということを考えていきたい。
'''
