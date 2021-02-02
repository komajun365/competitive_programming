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

import itertools

n,m = map(int,input().split())
a = [0] + list(map(int,input().split()))
cp = []
c_set = [set() for _ in range(m)]

for i in range(m):
    tmp = list(map(int,input().split()))
    cp.append(tmp[0])
    c_set[i] = set(tmp[2:])

ans = 0
for comb in itertools.combinations(range(1,n+1), 9):
    tmp = 0
    for i in comb:
        tmp += a[i]
    for j in range(m):
        cnt = 0
        for i in comb:
            cnt += (i in c_set[j])
            if(cnt >= 3):
                tmp += cp[j]
                break
    ans = max(ans,tmp)

print(ans)


'''
16C9 = 11440

全探索できそうです。
11440 * 50 * 9 = 5*10**6
'''
