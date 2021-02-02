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
s = [input() for _ in range(h)]

decode = [['.'] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        flag = True
        for x in range(3):
            x += i-1
            for y in range(3):
                y += j-1
                if x < 0 or y < 0 or x >= h or y >= w:
                    continue
                if s[x][y] == '.':
                    flag = False
        if flag :
            decode[i][j] = '#'

encode = [['.'] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        for x in range(3):
            x += i-1
            for y in range(3):               
                y += j-1
                if x < 0 or y < 0 or x >= h or y >= w:
                    continue
                if decode[x][y] == '#':
                    encode[i][j] = '#'

# print(decode)
# print(encode)

for i in range(h):
    for j in range(w):
        if s[i][j] != encode[i][j]:
            print('impossible')
            exit()

print('possible')
for di in decode:
    print(*di, sep='')