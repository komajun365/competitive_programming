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
w = list(map(int,input().split()))
b = list(map(int,input().split()))

max_b = 50 + 51 * 25
med = [[0] * (max_b+1) for _ in range(51)]

for wi in range(51):
    for bi in range(max_b+1):
        if wi == 0 and bi <= 1:
            continue

        move = [0] * max_b
        if wi != 0 and bi+wi <= max_b:
            move[med[wi-1][bi+wi]] = 1
        for k in range(1,bi//2 + 1):
            move[med[wi][bi-k]] = 1
        
        for i in range(max_b):
            if move[i] == 0:
                med[wi][bi] = i
                break

xor = 0
for wi,bi in zip(w,b):
    xor ^= med[wi][bi]

if xor == 0:
    print('Second')
else:
    print('First')
