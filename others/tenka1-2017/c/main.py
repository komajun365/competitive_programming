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

N = int(input())

for h in range(1,3501):
    for n in range(1,3501):
        m = N*h*n
        c = 4*h*n-N*n-N*h
        if c > 0:
            if m % c == 0:
                w = m//c
                print(h,n,w)
                exit()