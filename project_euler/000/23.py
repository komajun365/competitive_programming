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

n = 28124
tot = [0] * n
for i in range(1,n):
    for j in range(i*2,n,i):
        tot[j] += i

overs = []
for i,j in enumerate(tot):
    if(i<j):
        overs.append(i)

print(len(overs))
print(overs[:20])

check = [True] * n
for i in overs:
    for j in overs:
        num = i+j
        if(num >= n):
            continue
        check[num] = False

ans = 0
for i,j in enumerate(check):
    ans += i*j
print(ans)


'''
とりあえず過剰数のリストを作る
約7000個だし、あとは全探索しましょう。
'''
