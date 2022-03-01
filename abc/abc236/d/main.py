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

from itertools import product
from collections import deque

n = int(input())
a = [list(map(int, input().split())) for i in range(2*n-1)]

p_list = [list(range(1,(n-i)*2)) for i in range(n)]

ans = 0
for p in product(*p_list):
    res = 0
    num = list(range(2*n))
    for pi in p:
        left = num[0]
        right = num[pi]
        num = num[1:pi] + num[pi+1:]
        res ^= a[left][right-left-1]
    ans = max(ans,res)
    
print(ans)


        
