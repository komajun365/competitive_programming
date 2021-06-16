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

a,b = map(int,input().split())
a += b
if a >= 15 and b >= 8:
    print(1)
elif a >= 10 and b >= 3:
    print(2)
elif a >= 3:
    print(3)
else:
    print(4)