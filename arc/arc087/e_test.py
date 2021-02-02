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

n = 1024
dp = [-1] * (n+1)
dp[0] = 0

def calc(x):
    if(dp[x] != -1):
        return dp[x]

    bit_len = x.bit_length()

    for j in range(bit_len-1,-1,-1):
        if(x >> j)&1:
            y = x
            for i in range(j,-1,-1):
                y = y^(1<<i)
                if(calc(y)==0):
                    dp[x] = 1
                    return dp[x]

    dp[x] = 0
    return dp[x]

for i in range(n+1):
    x = 0
    y = i
    calc(i)
    # print(i,bin(i),calc(i))

for i in range(32):
    print(i*8,(i+1)*8,bin(i*8))
    print(dp[i*8:(i+1)*8])

# for i in range(n):
#     if(dp[i]==0):
#         print(i,bin(i))
#     tmp = 0
#     x = i
#     while(x>0):
#         tmp ^= (x&15)
#         x//=16
#     if(tmp==0)|(tmp==5):
#         print(i)

# for i in range(n):
#     tmp = 0
#     x = i
#     while(x>0):
#         tmp ^= (x&15)
#         x//=16
#     if(tmp==0)|(tmp==5):
#         x = i
#         print(i)


'''
二部木で考えて、
先祖と子孫を消していくゲーム

何かを消したとき、常に残りは二部木の森になっている？

深さxの木に対する操作結果
・全消し
・深さx-1の木を残す
・深さx-1,x-2の木を残す
・深さx-1,...,x-iの木を残す
・深さx-1,...,1の木を残す

下から見ていって、
奇数なら先手の勝ち、偶数なら後手の勝ち。

が先手勝ちの状態で、次の桁が奇数なら

topが奇数なら先手の勝ち。
偶数なら、それより下の状態が先手勝利なら先手、それ以外は後手。

全部偶数のパターンだけ後手が勝てる、それ以外は負け？

初期状態の把握



'''
