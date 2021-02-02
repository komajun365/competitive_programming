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
f = open('p018_triangle.txt', 'r')
sys.stdin = f

x = 1
for i in range(1,101):
    x *= i

s = str(x)
ans = 0
for i in s:
    ans += int(i)

print(ans)

'''
なんか普通に計算できそうじゃないですか？
'''
