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

'''
BFSでいける
200=b11001000
128=b01111111

深さ15まで見れば十分。
O(15！)ぐらいか
いや、そんな単純じゃない・・・
新しい数字の生成方法が深さの２乗通りあるのでやばい


15=1+1+1+3+3+6

15=1+1+2+4+2+1

1,2,4,6,8,16,32,64,128

'''
