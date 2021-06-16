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

n,*ab = map(int,read().split())
a = ab[::2]
b = ab[1::2]

ans = 10**7
for i in range(n):
    for j in range(n):
        if i==j:
            ans = min(ans, a[i]+b[i])
        else:
            ans = min(ans , max(a[i],b[j]))

print(ans)
