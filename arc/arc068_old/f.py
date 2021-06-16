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
mod = 10**9 + 7

max = 10**4
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

#　1より前の食べ方
ans = 0
if(k==1):
    ans=1
else:
    for i in range(k-1):
        ans += com(k-2,i)**2
        ans %= mod
    ans *= com(n-1,k-1)
    ans %= mod

# 1より後ろの食べ方
if(k!=n):
    ans *=pow(2,n-k-1,mod)

ans %= mod
print(ans)
#
# for i in dp:
#     print(i)

'''
1-Nを増加列二つに分ける
増加列二つの後ろからカードを取ってく。

K番目が1


増加列を二つ混ぜて、
k-1個の要素を持つ数列を作る

com(n-1,k-1)

増加列を二つ混ぜる
後ろからLISした時に最大２？

12345678
21345687

21111121

22211221
23415786

22222221
23456781

51234678
21111111

x1xxxx8x
21211121

31245678
21111111

12453678
11221111

11112211

片方の増加列を使い切ると、
前からも食べられることを忘れていました。。。

いずれにせよ、１を食った後の話ですね。
残りのn-k枚について、前か後ろから食べる方法
→　DPすればいい？


'''
