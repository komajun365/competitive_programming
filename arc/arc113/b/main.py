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

a,b,c = map(int,input().split())

a = a % 10
cyc = []
x = a
for i in range(4):
    cyc.append(x)
    x = x*a % 10

ans = cyc[ (pow(b,c,4)-1)%4 ]
print(ans)