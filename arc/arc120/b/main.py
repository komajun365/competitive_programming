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
read = sys.stdin.read

h,w,*s = read().split()
h,w = int(h), int(w)
mod = 998244353

ans = 1
for i in range(h+w-1):
    cnt = [0,0,0]
    for x in range(h):
        y = i-x
        # print(i,x,y)
        if y >= w or y < 0:
            continue
        if s[x][y] == 'R':
            cnt[0] += 1
        elif s[x][y] == 'B':
            cnt[1] += 1
        else:
            cnt[2] += 1
    if cnt[0] > 0 and cnt[1] > 0:
        print(0)
        exit()
    if cnt[0] + cnt[1] == 0:
        ans *= 2
    ans %= mod
print(ans)    
