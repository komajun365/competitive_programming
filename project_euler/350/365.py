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

#エラストテネスの篩
#n以下の素数のリストを返却
#2n+1だけ見る : 10**7 でpython3:1400ms, pypy3:700msくらい
def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    primes_append = primes.append
    len_list = (n+1)//2
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_list):
        if(flags[i]):
            primes_append(i*2+1)
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return primes

primes_0 = sieve(5000)
primes = []
for i in primes_0:
    if(i > 1000):
        primes.append(i)

print(len(primes))

a_max,a_min = 10**18, 10**18-10**9
b_max,b_min = 10**9,0

def count_fac(x,p):
    res = 0
    while(x>=p):
        res += x//p
        x //=p
    return res

# cnt = []
# for i in primes:
#     cnt.append( (count_fac(a_max,i)-count_fac(a_min,i),
#                  count_fac(b_max,i)-count_fac(b_min,i)) )
#
# for i,p in zip(cnt,primes):
#     if(i[0]==i[1]):
#         i
#         # print(p)

def light_nck(up,down,mod):
    child = count_fac(a_max,mod)-count_fac(a_min,mod)
    mother = count_fac(b_max,mod)-count_fac(b_min,mod)
    if(child>mother):
        return 0

    while(True):
        exp = 0
        while( True ):
            mod_exp = pow(mod,exp)
            if(up//mod_exp == (up-down)//mod_exp):
                break
            exp += 1
        mod_exp = pow(mod,exp+1)

        up2 = down + (up - down)%mod_exp
        if(up==up2):
            break

        up = up2
        down = min(down, up-down)

    print(mod,up,down,exp)

    max_num = up+10
    fac, finv, inv = [0]*max_num, [0]*max_num, [0]*max_num

    def comInit(max_num):
        fac[0] = fac[1] = 1
        finv[0] = finv[1] = 1
        inv[1] = 1

        for i in range(2,max_num):
          fac[i] = fac[i-1]* i% mod
          inv[i] = mod - inv[mod%i] * (mod // i) % mod
          finv[i] = finv[i-1] * inv[i] % mod

    comInit(max_num)

    # 二項係数の計算
    def com(n,k):
        if(n < k):
            return 0
        if( (n<0) | (k < 0)):
            return 0
        return fac[n] * (finv[k] * finv[n-k] % mod) % mod

    res = com(up,down)
    if(res==0):
        print(up,down,mod)
    return res

rem = []
for i in primes:
    rem.append(light_nck(10**18,10**9, i))

# print(rem)

def ext_gcd(a,b):
    #ax+by=1となるx,yの組を返す。
    # print(a,b)
    a,b = max(a,b), min(a,b)
    if(a==1) & (b==0):
        return (1,0)
    q = a//b
    r = a%b
    y,x = ext_gcd(b,r)
    y -= q*x
    return(x,y)


ans = 0
len_p = len(primes)
# len_p = 4
for i in range(len_p-2):
    p = primes[i]
    print(p)
    for j in range(i+1,len_p-1):
        q = primes[j]
        rev = ext_gcd(q,p)[1]
        tmp = (rev * (rem[i]-rem[j]) * q + rem[j]) % (p*q)
        for k in range(j+1,len_p):
            r = primes[k]
            rev = ext_gcd(r,p*q)[1]
            ans += (( rev * (tmp-rem[k]) ) * r + rem[k]) % (p*q*r)
            if(ans != 0):
                print(ans)
                print(tmp)
                print(rev)
                print(i,j,k)
                print(p,q,r)
                print(rem[i],rem[j],rem[k])
                print(pow(r,(p*q)-1,(p*q)))
                print(ext_gcd(r,p*q))
                exit()

print(ans)


'''
0にならないですかね？

1-10**9の間にあるpの素因数の数と
(10**18-10**9+1)-10**18の間にあるpの素因数の数を比較する。

→　なりませんでした。

1,nCkのmod pを求めておき、
2,mod p*q*rを頑張って合成する。

・nCkについて。
頑張って小さくします。
この辺を参考にしました。
http://blog.thetheorier.com/entry/2015/07/27/113258

→　→　ここが怪しいっぽい。

・mod p*q*rの合成
a = x (mod p)
a = y (mod q) のとき。
a = kp+x = lq+y (mod p*q)とおく。





'''
