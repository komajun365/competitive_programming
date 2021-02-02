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
ans = ''

cnt = 0
while(n>0):
    ans = chr((n-1)%26 + ord('a')) + ans
    n = (n-1)//26

print(ans)

# def get_head(n):
#     x = n -1
#     minus = 0
#     cnt = 0
#     while(x>=26):
#         x //= 26
#         cnt += 1
#     s = chr(x + ord('a'))
#     if(cnt == 0):
#         return s,0
#     rem = n - (x+1) * (26**(cnt-1))
#     return s,rem
#
# while(n>0):
#     s,n = get_head(n)
#     ans = ans + s
#
# print(ans)
