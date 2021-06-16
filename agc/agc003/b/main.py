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

n,*a = map(int,read().split())
a += [0]

ans = 0
for i in range(n):
    ai = a[i]
    ans += ai//2
    if ai%2 == 1 and a[i+1] > 0:
        ans += 1
        a[i+1] -= 1

print(ans)