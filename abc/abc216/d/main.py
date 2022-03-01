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

n,m,*data = map(int,read().split())

a = []
idx = 0
for _ in range(m):
    ki = data[idx]
    ai = data[idx+1:idx+1+ki]
    a.append(ai[::-1])
    idx += 1 + ki

cnt = 0
num = [-1] * (n+1)
for i in range(m):
    stack = [i]
    while stack:
        x = stack.pop()
        if len(a[x]) == 0:
            continue 
        num_x = a[x].pop()
        if num[num_x] == -1:
            num[num_x] = x
        else:
            z = num[num_x]
            cnt += 1
            stack.append(x)
            stack.append(z)

if cnt == n:
    print('Yes')
else:
    print('No')

# print(a)



