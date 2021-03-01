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
read = sys.stdin.read

n,m,s,*data = read().split()
n = int(n)
m = int(m)
mod = 1000000007

## nCkのmodを求める関数
# テーブルを作る(前処理)
max_n = 3010
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

# 二項係数の計算
def com(n,k):
    if(n < k):
        return 0
    if( (n<0) | (k < 0)):
        return 0
    return fac[n] * (finv[k] * finv[n-k] % mod) % mod

cnt = [0] * (n+1)
for i in range(n):
    cnt[i] = cnt[i-1] + 1 * (s[i] == '1')

# print(s)
# print(cnt)

lr = []
it = iter(data)
for l,r in zip(it,it):
    l = int(l)-1
    r = int(r)-1
    if lr:
        if r <= lr[-1][1]:
            continue
        if l == lr[-1][0]:
            lr[-1][1] = r
        else:
            lr.append([l,r])
    else:
        lr.append([l,r])

m = len(lr)
lr.append([n+10,n+10])

dp = [1]
done = -1
for i in range(m):
    l,r = lr[i]
    l2 = lr[i+1][0]

    len1 = len(dp)
    len2 = max(1, r-l2 + 2)
    set_l = min(r+1,l2) - l
    dp2 = [0] * len2

    if done < l:
        done = l-1
    ones = cnt[r] - cnt[done]
    for x1 in range(len1):
        for x2 in range(len2):
            use = x1 + ones - x2
            # print(set_l,ones, x1,x2,use)
            if use < 0 or use > set_l:
                continue
            dp2[x2] += dp[x1] *  com(set_l, use) % mod
            dp2[x2] %= mod
    dp,dp2 = dp2,dp
    done = r
    # print(i,l,r,l2,len1,len2,set_l)
    # print(dp)

print(dp[0])




