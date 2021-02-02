import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# 方針
# 最小の転倒数をbitdpで更新していく。
# 状態は（mask,k）で、maskは2**nのbitフラグ。kは0~(n-1）
# maskに含むカードを並び替えた後で、最後にk番目のカードを置いたときの最小の転倒数をいれる。
# 転倒数は最大17C2＝153ぐらいなので、単調増加できない場合は10000をつっこんでおく。

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[-1] * n for _ in range(1 << n)]

def calc_ans(mask, k):
    if(dp[mask][k] != -1):
        return dp[mask][k]

    # mask内の1が立ってるbitの本数確認
    # maskが空なら転倒数0を返す
    if( bin(mask).count('1') == 0 ):
        dp[mask][k] = 0
        return 0

    # maskが空じゃない場合
    min = 10000
    for i in range(n):
        # i番目のフラグが1なら手前を見に行く
        if( (mask & 1<<i) >> i == 1):
            mask_b =



for i in range(6):
    print((57 & 1 << i) >>i)
bin(57)

bin( 57 ^ 1<<3)
bin( 57 ^ 1<<2)
