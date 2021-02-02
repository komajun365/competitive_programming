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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,*xy = map(int,read().split())

for i in range(n-2):
    xi,yi = xy[i*2:i*2+2]
    for j in range(i+1,n-1):
        xj,yj = xy[j*2:j*2+2]
        for k in range(j+1,n):
            xk,yk = xy[k*2:k*2+2]

            if((xj-xi)*(yk-yi) == (xk-xi)*(yj-yi)):
                print('Yes')
                exit()

print('No')
