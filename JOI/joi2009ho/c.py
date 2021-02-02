# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# 検討分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline

n,m,h,k = map(int,input().split())
point = [int(input()) for _ in range(n)]

lines = [tuple(map(int,input().split())) for _ in range(m)]
lines = sorted(lines, key=lambda x: x[1])

scores = point[::]
for line in lines[::-1]:
    y = line[0]-1
    scores[y],scores[y+1] = scores[y+1],scores[y]

minus = 0
move = list(range(1,n+1))
for line in lines:
    y = line[0]-1
    left = move[y]
    right = move[y+1]
    if((left<=k)&(right>k)):
        minus = min(minus, scores[right-1] - scores[left-1])
    elif((left>k)&(right<=k)):
        minus = min(minus, scores[left-1] - scores[right-1])
    move[y],move[y+1] = move[y+1],move[y]

ans = sum(scores[:k]) + minus
print(ans)

'''
方針
棒を消さない場合の点数を計算するO(M)
消したときに点数が変化する棒を見ていって、
最大の差が利幅のものを選ぶO(N)
'''
