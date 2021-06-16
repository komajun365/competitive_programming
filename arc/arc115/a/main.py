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

n,m,*s = read().split()
n = int(n)
m = int(m)

odd = 0
even = 0
for si in s:
    if si.count('0') % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd * even)
