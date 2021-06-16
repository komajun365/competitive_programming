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

h,w = map(int,input().split())
w_chr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(1,h+1):
    s = input().split()
    for j in range(w):
        if s[j] == 'snuke':
            print(w_chr[j],i,sep='')
            exit()