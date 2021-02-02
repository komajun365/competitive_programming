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

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

n,m = map(int,input().split())

'''
DFSしつつ確率計算

・到達
p

・撤退
1-p

と思ったけど、思ったより難しそう

＝＝＝＝＝＝

各海域から、ゴールにたどり着けるまでの消費HPと確率を計算しておく
（海域番号の降順にチェックすればOK）

逆に、スタートからたどり着くまでの消費HPと確率も管理できる。




'''
