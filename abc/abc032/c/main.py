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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,k,*s = map(int,read().split())

if 0 in s:
    print(n)
    exit()

if(min(s) > k):
    print(0)
    exit()

s += [0]

ans = 1
num = s[0]
l = 0
r = 0
while(r < n):
    if(num > k):
        num //= s[l]
        l += 1
    else:
        ans = max(ans, r-l+1)
        r += 1
        num *= s[r]

print(ans)






