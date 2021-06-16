# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

# https://atcoder.jp/contests/tokiomarine2020/submissions/20029669

def solve(wv1,wv2,W):
    W = (W+1)*M
    ans = 0
    idx = len(wv1)-1
    for wv in wv2:
        while idx >= 0 and wv1[idx]+wv >= W:
            idx -= 1
        if idx >= 0 and (wv1[idx]+wv)%M > ans:
            ans = (wv1[idx]+wv)%M
    return ans   

# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

M = 2**25
A = 11

n = int(readline())
wv = [0]*(n+1)
for i in range(1,n+1):
    v,w = map(int,readline().split())
    wv[i] = w*M+v

N = min(1<<A,n+1)
memowv = [None]*N
memowv[0] = [0]

for i in range(1,N):
    lst = memowv[i] = memowv[i//2]*2
    for j in range(len(lst)//2):
        lst[j] += wv[i]
    lst.sort()
    for j in range(1,len(lst)):
        v2 = lst[j]%M
        v1 = lst[j-1]%M
        if v1 > v2: lst[j] += v1-v2

print(memowv)

q, = map(int,readline().split())
for _ in range(q):
    u,l = map(int,readline().split())
    lst = [0]
    while u >= N:
        lst *= 2
        for i in range(len(lst)//2): lst[i] += wv[u]
        lst.sort()
        u //= 2
    print(solve(memowv[u],lst,l))














