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

t,*case = map(int,read().split())
ans = []
it = iter(case)
for l,r in zip(it,it):
    x = r - 2*l + 1
    if x < 0:
        ans.append(0)
    else:
        ans.append( x*(x+1)//2 )

print('\n'.join(map(str,ans)))