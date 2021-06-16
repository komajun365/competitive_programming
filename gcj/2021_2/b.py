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

# tmp = 0
# for i in range(3,10**6+1):
#     tmp += 10**6//i
# print(tmp)

import sys
read = sys.stdin.buffer.read


t,*data = map(int,read().split())

max_n = max(data)
cnt = [-1] * (max_n+1)
for i in range(2,max_n+1):
    if cnt[i]== -1:
        cnt[i] = 1
    j = 2
    while True:
        tmp = j * (i+1)
        if tmp > max_n:
            break
        cnt[tmp] = max(cnt[tmp], cnt[i] + 1)
        j += 1

ans = [''] * t
for i in range(t):
    n = data[i]
    res = 1
    for j in range(3,1001):
        if j**2 > n:
            break
        if n % j == 0:
            res = max(res, cnt[j - 1] + 1)
            res = max(res, cnt[n//j - 1] + 1)

    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))

# print(cnt)

for n in range(3,42):
    res = 1
    for j in range(3,1001):
        if j**2 > n:
            break
        if n % j == 0:
            res = max(res, cnt[n//j - 1] + 1)
    # print(n,p,res)

    print(n,res)

# print(cnt[:10])
# print(cnt[10:20])
# print(cnt[20:30])
# print(cnt[30:40])