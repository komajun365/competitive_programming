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
f = open('p107_network.txt', 'r')
sys.stdin = f

n = 15
# hoge = 1
# for i in range(8):
#     hoge *= n-i
#
# for i in range(8):
#     hoge //= i+1
#
# print(hoge)

games = 1
for i in range(n):
    games *= i+2

wins = 0
for i in range(2**n):
    bit_count = 0
    for j in range(n):
        if((i>>j)&1):
            bit_count += 1

    if(bit_count >= 8):
        tmp = 1
        for j in range(n):
            if not ((i >> j)&1):
                tmp *= j+1
        wins += tmp

print(games)
print(wins)
print(games//wins)


'''
めんどくさいですね

15C8 =
15C9 =

８勝以上できる確率を計算していく。
包徐原理というかなんというか・・・。

あ、bit全探索でよいですね。

'''
