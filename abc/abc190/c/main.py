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
n,m,*data = map(int,read().split())

ab = data[:2*m]
k = data[2*m]
cd = data[2*m+1:]

ans = 0
for i in range(1<<k):
    ball = [0] * (n+1)
    for j in range(k):
        if (i >> j) & 1:
            ball[ cd[j*2 + 1] ] += 1
        else:
            ball[ cd[j*2 ] ] += 1
    
    tmp = 0
    it = iter(ab)
    for a,b in zip(it,it):
        if ball[a] > 0 and ball[b] > 0:
            tmp += 1

    ans = max(tmp,ans)

print(ans)

