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

n = int(input())
mod = 10**9 + 7

n_bit = []
x = n
while(x>0):
    n_bit.append(x%2)
    x //= 2
n_bit = n_bit[::-1]

n_len = len(n_bit)

dp = [[0] * 3 for _ in range(n_len+1)]
dp[0][0] = 1

for i,bi in enumerate(n_bit):
    if(bi == 0):
        dp[i+1][0] += dp[i][0] + dp[i][1]
        dp[i+1][1] += dp[i][1]
        dp[i+1][2] += dp[i][1] + dp[i][2]*3
    else:
        dp[i+1][0] += dp[i][0]
        dp[i+1][1] += dp[i][0] + dp[i][1]
        dp[i+1][2] += dp[i][1]*2 + dp[i][2]*3
    dp[i+1][0] %= mod
    dp[i+1][1] %= mod
    dp[i+1][2] %= mod

ans = sum(dp[-1]) % mod
print(ans)



'''
a+b=vについて、
a xor b = u が何通りあるか？という話？

あるいは
a xor b = uについて
a+b <= nがいくつあるか？　というはなし？

1の個数

1,0,0,2,1,0

100110
000100

桁DPっぽい


3
11
10
00
01
02

普通の2進数ならば、
下からi桁目を決めた時、
残りの数字は2**i未満になっていないといけない。

今回の場合は、
2**i + 2**(i-1)未満になっていればなんとかなる。

上から二けたを見たとき
残り - 一番上の桁 - 次の残り
0-0-0*2+x
1-0-1*2+x
2-0-2*2+x
2-1-0*2+x
3-0 - 残りが全部0の時だけOK
3-1-1*2+x

'''
