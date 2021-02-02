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
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n = int(readline())
s = read().split()

ans = []
for si in s:
    ans.append([])
    for ci in si:
        ans[-1].append(ci)

# print(ans)

for i in range(n-2,-1,-1):
    for j in range(1,2*n-2):
        # print(i,j)
        if(ans[i][j] == '.'):
            continue
        for d in [-1,0,1]:
            if(ans[i+1][j+d] == 'X'):
                ans[i][j] = 'X'

for ai in ans:
    print(''.join(ai))