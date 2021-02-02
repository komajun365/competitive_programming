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
for a in range(1,100):
    na = 3**a
    for b in range(1,100):
        nb = 5**b
        if(na + nb == n):
            print('{} {}'.format(a,b))
            exit()
        if(na + nb > n):
            break

print(-1)