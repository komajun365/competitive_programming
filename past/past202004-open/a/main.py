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


s,t = input().split()
def calc(x):
    if('B' == x[0]):
        res = 9 - int(x[1])
    else:
        res = 8 + int(x[0])
    return res

ans = abs( calc(s) - calc(t) )
print(ans)