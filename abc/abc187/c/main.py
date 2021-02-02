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

n,*s = read().split()
n = int(n)
s0 = set()
s1 = set()
for si in s:
    if(si[0] == '!'):
        s1.add(si[1:])
    else:
        s0.add(si)

for si in s0:
    if si in s1:
        print(si)
        exit()


print('satisfiable')