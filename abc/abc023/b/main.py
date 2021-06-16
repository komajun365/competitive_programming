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

n = int(input())
s = input()

x = (n-1)//2
t = 'b'
for i in range(x):
    if i%3==0:
        t = 'a' + t + 'c'
    elif i%3==1:
        t = 'c' + t + 'a'
    else:
        t = 'b' + t + 'b'

if t == s:
    print(x)
else:
    print(-1)
