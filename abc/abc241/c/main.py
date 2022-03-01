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
s = [input() for _ in range(n)]

s2 = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == '#':
            s2[i][j] = 1

def end():
    print('Yes')
    exit()

def rotate(x):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if x[i][j] == 1:
                res[j][n-i-1] = 1
    return res

for _ in range(4):
    # tate
    for i in range(n):
        cnt = 0
        for j in range(n):
            cnt += s2[i][j]
            if j >= 6:
                cnt -= s2[i][j-6]
            if cnt >= 4:
                end()
    # naname
    for i in range(n-6):
        cnt = 0
        for j in range(n-i):
            cnt += s2[i+j][j]
            if j >= 6:
                cnt -= s2[i+j-6][j-6]
            if cnt >= 4:
                end()
    s2 = rotate(s2)

print('No')

# # yoko
# for j in range(n):
#     cnt = 0
#     for i in range(n):
#         if s[i][j] == '#':
#             cnt += 1
#         if j >= 6:
#             if s[i-6][j] == '#':
#                 cnt -= 1
#         if cnt >= 4:
#             end()

