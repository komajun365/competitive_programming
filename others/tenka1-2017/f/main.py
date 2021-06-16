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

import sys
read = sys.stdin.buffer.read
from math import gcd
sys.setrecursionlimit(10**9)

def inv_gcd(a, b):
    """
    g = gcd(a, b), xa = g (mod b), 0 <= x < b/g
    を満たすような[g, x]を計算する。
    特にg = gcd(a, b) = 1 の時、
    xはbを法としたときのaの逆元である。
    a = 0 の場合は[b, 0]を返却する。

    Parameters
    ----------
    a : int
    b : int
        b >= 1

    Returns
    -------
    [s, m0] : list
    """
    a %= b
    if a == 0:
        return [b, 0]

    s, t = b, a
    m0, m1 = 0, 1
    while t:
        u = s // t
        s -= t * u
        m0 -= m1 * u
        s, t = t, s
        m0, m1 = m1, m0

    if m0 < 0:
        m0 += b // s
    return [s, m0]

def inv_mod(x, m):
    """
    mを法としたときのxの逆元を計算する。

    Parameters
    ----------
    x : int
    m : int
        m >= 1 かつ x,mは互いに素

    Returns
    -------
    int
        mを法としたときのxの逆元
    """
    assert 1 <= m
    z = inv_gcd(x, m)
    assert z[0] == 1
    return z[1]


def crt(r, m):
    """
    中国余剰定理（Chinese Remainder Theorem, CRT）の計算
    len(r) = nとしたときに、
    全てのi(0 <= i < n)について、
    r[i] == x % m[i]を満たすxを計算する。

    Parameters
    ----------
    r : list = [int * n]
    m : list = [int * n]
        len(r) == len(m)
        1 <= m[i]

    Returns
    -------
    [r0, m0] : list
        答えが存在しない場合、[0, 0]
        len(r) == 0の時、[0,1]を返却する。
        それ以外の場合、
        全てのi(0 <= i < n)について、
        r[i] == x % m[i]を満たすxを計算し、
        x = r0 % m0が成り立つ[r0, m0]の組を返却する。
        m0 = lcm(m[i])となる。
    """
    assert len(r) == len(m)
    n = len(r)

    r0, m0 = 0, 1
    for i in range(n):
        assert 1 <= m[i]
        r1 = r[i] % m[i]
        m1 = m[i]
        if m0 < m1:
            r0, r1 = r1, r0
            m0, m1 = m1, m0
        if m0 % m1 == 0:
            if r0 % m1 != r1:
                return [0, 0]
            continue

        g, im = inv_gcd(m0, m1)
        u1 = m1 // g
        if (r1 - r0) % g:
            return [0, 0]

        x = (r1 - r0) // g % u1 * im % u1
        r0 += x * m0
        m0 *= u1
        if r0 < 0:
            r0 += m0
    return [r0, m0]

# 素因数分解
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
        if temp==1:
            break

    if(temp != 1):
        arr.append([temp, 1])
    
    return arr

q,*am = map(int,read().split())

def calc(a,m):
    # a^x % m == 0
    if pow(a,64,m) == 0:
        return 64 * m
    
    a %= m
    gcd_num = 1
    x = 0
    a2 = 1
    while True:
        a2 = a2 * a % m
        gcd_num2 = gcd(a2, m)
        if gcd_num == gcd_num2:
            break
        gcd_num = gcd_num2
        x += 1
    
    m2 = m // gcd_num
    factor = factorization(m2)
    phi = m2
    for p,_ in factor:
        phi *= (p-1)
        phi //= p
    
    x = calc(a, gcd(m, phi))
    # print(x)
    x = -(-x//phi) * phi + x%phi
    # print(a,m,phi,x)
    a2 = pow(a,x,m)
    # print(x,a2,phi,m)
    res = crt([x,a2],[phi,m])
    if res[0] < x:
        res[0] += -(-x//res[1]) * res[1]
    return res[0]



it = iter(am)
for a,m in zip(it,it):
    res = calc(a,m)
    print(res)
    # print('chack: ', res, pow(a,res,m), res % m)

# for i in range(60):
#     print(i, pow(177,i,168))  
    


'''

x = k(mod phi)
a**x = k (mod m)

g = gcd(phi,m)

a ** x = x mod g
calc(a,g)

'''