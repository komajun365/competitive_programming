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

h,w,*a = map(int,read().split())
ans = []
for i in range(w):
    tmp = []
    for j in range(h):
        tmp.append(a[j*w+i])
    ans.append(' '.join(map(str,tmp)))
print(*ans, sep='\n')
