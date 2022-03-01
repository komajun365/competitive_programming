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

x = input()

if x[0] == x[1] == x[2] == x[3]:
    print('Weak')
    exit()

base = '01234567890123456789'
for i in range(10):
    if base[i:i+4] == x:
        print('Weak')
        exit()

print('Strong')