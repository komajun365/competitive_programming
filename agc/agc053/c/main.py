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
mod = 10**9 + 7

max_n = n + 10
fac, finv, inv = [0]*max_n, [0]*max_n, [0]*max_n

def comInit(max_n):
    # fac[0] = fac[1] = 1
    # finv[0] = finv[1] = 1
    inv[1] = 1

    for i in range(2,max_n):
    #   fac[i] = fac[i-1]* i% mod
      inv[i] = mod - inv[mod%i] * (mod // i) % mod
    #   finv[i] = finv[i-1] * inv[i] % mod

comInit(max_n)

dp = [0] * (n+1)
dp2 = [0] * (n+1)
tot = 0

for i in range(1,n+1):
    dp[i] = (tot*inv[2] + i*(i+1)//2)% mod * inv[i] % mod
    dp2[i] = (tot*inv[2] + i*(i+1))% mod * inv[i] % mod
    tot += dp[i] + dp2[i]
    tot %= mod

print(dp[-1])

print(dp)
print(dp2)

print(27 * inv[12] % mod)
print(45 * inv[12] % mod)

'''

dp[i]
2nがどの高さにあるか。
jにあるとすると、j~nまでは消せる。
山の高さj-1になる。
m = j-1として似たような問題に帰着できる。
・2mが2nと同じ山にある場合
→　残りの回数の期待値はdp[m]
・2mが2nと違う山にある場合
→
2mを消しに行く必要がある。

dp2[i]をそっちの問題にしておこう。
2nがｊの高さにあるとき、
infのある山を高さj-1まで削る。
すると、2nが消せる。
残りは
・2mが2nと同じ山にある場合
→　残りの回数の期待値はdp[m]
・2mが2nと違う山にある場合
→　残りの回数の期待値はdp[2m]


dp[0],dp2[0] = 0
dp[1] = 1
dp2[1] = 2

dp[i] = (1/n) * sum((dp[j]+dp2[j])/2 + (i-j) (j=0~i-1))
dp2[i] = (1/n) * sum((dp[j]+dp2[j])/2 + (i-j)*2 (j=0~i-1))


'''