# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討9分　実装11分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

from sys import stdin
read = stdin.buffer.read
readline = stdin.buffer.readline
readlines = stdin.buffer.readlines

k,m = map(int,readline().split())
s = readline().rstrip().decode()
cba = list(map(int,read().split()))
n = cba[-1]

ans = list(range(k))

it = iter(cba[::-1])
for left,b,a in zip(it,it,it):
    width = b-a
    right = left+width
    for ind,num in enumerate(ans):
        if(  left <= num < right ):
            ans[ind] = a + (num-left)
        elif( right <= num ):
            ans[ind] -= width

ans_s = []
for i in ans:
    ans_s.append(s[i])

print(''.join(ans_s))


'''
後ろから戻っていく。
最終的にx番目にいるアルファベットは、
その1手前にどこにいたか。


Ai,Bi,Ci
・x < Ciなら
x　→　x

・Ci <= x < Ci+(Bi-Ai)なら
x → Ai～Bi

・Ci+(Bi-Ai) <= xなら
x → x-(Bi-Ai)

一個一個追って行ってもO(KN)で間に合いそう。
'''
