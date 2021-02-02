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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
p = [[int(j),i] for i,j in enumerate(read().split()) ]
p.sort()

longest = 1
now = 1
for i in range(1,n):
    if(p[i][1] > p[i-1][1]):
        now += 1
    else:
        now = 1
    longest = max(longest,now)

print(n-longest)

'''
N回あればどうとでもなる。
もうちょい少なめに行きたい。

前に飛ばすグループ
→　1~iまでの数字
後ろに飛ばすグループ
→　j~ｎまでの数字。

i+1~j-1までは、
昇順に並んでいる部分列として最大の長さのものとすればよい。

1-nまでのindexを求めて、増加し続けているものの長さの最大値をgetすればOK。
ソートするので、O(nlogN)でいけますね。

'''
