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

n,k = map(int,input().split())
a = list(map(int,input().split()))
mod  = 10**9 + 7

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


left = [1] * (n+1)
# right = [1] * (n+2)

for i in range(2,n+1):
    left[i] = (left[i-1] * (k+i-1) * inv[i-1])%mod
    # right[n+1-i] = (right[n+2-i] * (k+i-1) * inv[i])%mod

ans = 0
for i,ai in enumerate(a,1):
    tmp = (ai * left[i] * left[-1*i])%mod
    ans += tmp
    ans %= mod

print(ans)
# print(left)

'''

最終的にどんな数列にもできる。
ので、各数列にたどり着く操作回数がわかればよい？

k回でl,rにたどり着く方法の数
→　 (k-1 + l-1)C(l-1) * (k-1 + n-r)C(n-r)

l,rが独立でないのが面倒である。。。

逆に考える。
Aiが生き残るパターン。
Σ(k-1 + x-1)C(x-1) * (k-1 + n-y)C(n-y)
 = (k-1 + i)C(i-1) * (k-1 + n-i+1)C(n-i)

1 <= x <= i
i <= y <= n

いけそうです！

と思ったが、Kがでかい・・・
左側にしかでてこないのでなんとかなるか？


'''
