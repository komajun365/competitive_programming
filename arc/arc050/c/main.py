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

a,b,m = map(int,input().split())

g = gcd(a,b)

ex10 = [1,10%m]
for i in range(1,60):
    ex10.append(pow(ex10[-1],2,m))

ex1 = [1,1]
for i in range(1,60):
    ex1.append( ex1[-1] * (1 + ex10[i]) % m)

def get_ex(x,ex):
    res = 0
    for i in range(60):
        if (x >> i) & 1:
            res *= ex10[i+1]
            res %= m
            res += ex[i+1]
            res %= m
    return res

def calc_ag(a,g):
    if a == g:
        return 1
    
    if (a // g) % 2 == 0:
        base = calc_ag(a//2,g)
        res = base + base * pow(10,a//2,m)
        res %= m
    else:
        a1 = a-g
        base = calc_ag(a1//2,g)
        res = base + base * pow(10,a1//2,m)
        res %= m
        res *= pow(10,g,m)
        res = (res + 1) % m
    return res

ans = calc_ag(a,g) * get_ex(b,ex1) % m
print(ans)


