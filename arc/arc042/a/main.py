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

n,m,*a = map(int,read().split())

ans = []
rem = set(range(1,n+1))
a = list(range(n,0,-1)) + a

for ai in a[::-1]:
    if ai in rem:
        ans.append(ai)
        rem.remove(ai)

print('\n'.join(map(str,ans)))