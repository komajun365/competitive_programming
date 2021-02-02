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

b,w = map(int,input().split())
mod = 10**9 + 7

## nCkのmodを求める関数
# テーブルを作る(前処理)
max = 2 * 10**5 + 100
fac, finv, inv = [0]*max, [0]*max, [0]*max

def comInit(max):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max)

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

def solve(b,w):
    ans = []
    ex2 = 1
    b_end = 0
    w_end = 0
    n = b+w
    for i in range(n):
        if(i >= b):
            b_end = (b_end*2 + com(i-1,i-b) )%mod
        if(i >= w):
            w_end = (w_end*2 + com(i-1,i-w) )%mod

        bw = (ex2 - b_end - w_end)% mod
        ex2 = (ex2*2)%mod
        ans.append( (w_end*2 + bw) * pow(ex2,mod-2,mod) % mod )
        # print(bw,b_end,w_end)
        # print((w_end*2 + bw),ex2)

    # print(ans)
    return ans

def solve_simple(b,w):
    n = b+w
    blacks = [0] * n
    for i in range(2**n):
        x,y = b,w
        for j in range(n):
            if((i>>j)&1):
                if(x > 0):
                    blacks[j] += 1
                    x -= 1
                else:
                    y -= 1
            else:
                if(y>0):
                    y -= 1
                else:
                    blacks[j] += 1
                    x -= 1

    # print(blacks)
    ex2_inv = pow(2**n,mod-2,mod)
    for i in range(n):
        blacks[i] = (blacks[i]*ex2_inv)%mod

    return blacks

import random
for _ in range(100):
    b = random.randint(1,7)
    w = random.randint(1,7)
    ans1 = solve(b,w)
    ans2 = solve_simple(b,w)
    for i,j in zip(ans1,ans2):
        if(i!=j):
            print(b,w)
            print(ans1)
            print(ans2)
            exit()





'''
p(i,j) := blackがi個、whiteがj個出たとこにたどり着く確率

DPはできるけど計算量が多い

blackがi個、whiteがj個出たとして
(i+j)Ci となったとき、
・ j >= w
ホワイト使い切っているので、次は全部黒とみなしていい
Σ　mCi (0<=i <= m-w) =

・ i >= b
ブラック使いきっているので、次は全部白とみなしてよい

・上記以外
次は黒と白と同確率



'''
