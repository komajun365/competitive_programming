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

import sys
read = sys.stdin.buffer.read

R,C,k,n,*rc = map(int,read().split())

r_num = [0] * R
c_num = [0] * C

it = iter(rc)
for r,c in zip(it,it):
    r -= 1
    c -= 1
    r_num[r] += 1
    c_num[c] += 1

cnt_c = dict()
for ci in c_num:
    if ci in cnt_c:
        cnt_c[ci] += 1
    else:
        cnt_c[ci] = 1

ans = 0
for ri in r_num:
    if k - ri in cnt_c:
        ans += cnt_c[k - ri]

it = iter(rc)
for r,c in zip(it,it):
    r -= 1
    c -= 1
    if r_num[r] + c_num[c] == k:
        ans -= 1
    elif r_num[r] + c_num[c] == k+1:
        ans += 1

print(ans)