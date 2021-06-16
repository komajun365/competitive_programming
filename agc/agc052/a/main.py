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

t,*b = read().split()
ans = []
it = iter(b)
for n,s1,s2,s3 in zip(it,it,it,it):
    n = int(n)
    ans.append('0'*n + '1'*n + '0')
  
print('\n'.join(ans))
