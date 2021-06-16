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
A,B,C,*d=map(int,sys.stdin.read().split())
x=[0]*(99)
C+=1
x[0]=1/C
for i in range(B):
 for j in range(B,-1,-1):
  x[j]=(x[j]*(C+i-j)+x[j-1]*j*d[A+i])/(C+i+1)
print(sum(x)*sum(d[:A]))
