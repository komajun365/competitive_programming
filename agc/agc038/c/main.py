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

n = int(input())
a = list(map(int,input().split()))
mod = 998244353

a_max = 10**6

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = a_max + 10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
      fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
      finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)

coef = list(range(a_max+1))
div_first = [-1] * (a_max+1)
for i in range(2,a_max+1):
    dif = 1 - coef[i]
    coef[i] = dif
    if(div_first[i] == -1):
        div_first[i] = i
    for j in range(i*2,a_max+1,i):
        coef[j] += dif * (j//i)
        if(div_first[j] == -1):
            div_first[j] = i

cnt = [0] * (a_max+1)
for ai in a:
    cnt[ai] += 1

sum1 = [0] * (a_max+1)
sum2 = [0] * (a_max+1)

sum1[1] += cnt[1]
sum2[1] += cnt[1]

for i in range(2,a_max+1):
    if(cnt[i] == 0):
        continue
    
    factor = dict()
    x = i
    while(x > 1):
        y = div_first[x]
        if(y in factor):
            factor[y] += 1
        else:
            factor[y] = 1
        x //= y
    divs = [1]
    for key,val in factor.items():
        l = len(divs)
        for j in range(val):
            mul = key**(j+1)
            for k in range(l):
                divs.append( divs[k] * mul )
    
    add1 = cnt[i] * i % mod
    add2 = cnt[i] * (i**2) % mod
    for j in divs:
        sum1[j] += add1
        sum1[j] %= mod
        sum2[j] += add2
        sum2[j] %= mod

ans = 0
for i in range(1,a_max+1):
    tmp = pow(sum1[i],2,mod)
    tmp -= sum2[i]
    tmp *= inv[2] * inv[i]
    tmp %= mod
    tmp *= coef[i]
    tmp %= mod
    ans += tmp
    ans %= mod

print(ans)

# print(sum1[:20])
# print(sum2[:20])


