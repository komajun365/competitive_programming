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

import sys
read = sys.stdin.read

h,w,*s = read().split()
h = int(h)
w = int(w)

red = [['.'] * w for _ in range(h)]
blue = [['.'] * w for _ in range(h)]
for j in range(w):
    red[0][j] = '#'
    blue[-1][j] = '#'

for j in range(0,w,2):
    for i in range(1,h-1):
        red[i][j] = '#'

for j in range(1,w,2):
    for i in range(1,h-1):
        blue[i][j] = '#'

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            red[i][j] = '#'
            blue[i][j] = '#'

print('\n'.join(map(lambda x: ''.join(x), red)))
print('')
print('\n'.join(map(lambda x: ''.join(x), blue)))

# check
# s2 = [''] * h
# for i in range(h):
#     for j in range(w):
#         if red[i][j] == blue[i][j] == '#':
#             s2[i] += '#'
#         else:
#             s2[i] += '.'
#     if s2[i] != s[i]:
#         print('fail')