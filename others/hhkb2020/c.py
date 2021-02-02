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
p = list(map(int,input().split()))

used = [0] * (2*10**5+10)
tmp = 0
ans = []
for pi in p:
    used[pi] = 1
    while(used[tmp] == 1):
        tmp += 1
    ans.append(tmp)

print('\n'.join(map(str,ans)))
