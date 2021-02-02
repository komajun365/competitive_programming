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
c = input()
ans = c.count('R')
ans = min(ans, c[:ans].count('W'))

print(ans)


'''
WR を消したい

全部Wにする
全部Rにする
R...RW...にする

W -> Rは右に持っていくのと同じ
R ->Wだけ考えればよい？

'''
