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
s = [ input() * 2 for _ in range(n)]

ans = 0
for k in range(n):
    check = 1
    for i in range(n-1):
        for j in range(i+1,n):
            if(s[i][j+k] != s[j][i+k]):
                check = 0
                break
        if(check==0):
            break
    ans += check * n

print(ans)




'''
全探索ですね。
Nパターン　*　探索コストN**2


'''
