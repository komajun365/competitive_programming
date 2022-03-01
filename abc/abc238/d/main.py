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
for a,s in zip(it,it):
    if 2*a > s:
        ans.append('No')
        continue
    if (s-2*a) & a == 0:
        ans.append('Yes')
    else:
        ans.append('No')
print(*ans, sep='\n')