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
f = open('names.txt', 'r')
sys.stdin = f

s = list(map(lambda x: x.strip('\"'), input().split(',')))
print(s[:10])
s.sort()
print(s[:10])

ans = 0
for ind,si in enumerate(s,1):
    score = 0
    for ch in si:
        score += ord(ch) - ord('A') + 1
    ans += ind*score

print(ans)

'''
O(NlogN)ぐらいで全探索できます

'''
