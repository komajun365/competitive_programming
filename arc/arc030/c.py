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

有向辺を張りなおす。
と思ったが、自分に戻ってこれるパターンが厄介。

頂点300個なので、ひとまず全ての頂点対について、
辞書順の移動ができるかどうか考える。






'''
