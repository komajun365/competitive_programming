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
r,c = map(int,input().split())
import sys
read = sys.stdin.read
s = read().split()

arrow = '><v^'

n = h*w
links = [[] for _ in range(n)]
ans = [['x'] * w for _ in range(h)]
for i in range(n):
    x = i//w
    y = i%w
    si = s[x][y]
    if si == '#':
        ans[x][y] = '#'
        continue
    for cnt,x1,y1 in zip([0,1,2,3],[0,0,-1,1],[-1,1,0,0]):
        x1 += x
        y1 += y
        if x1 < 0 or x1 >= h or y1 < 0 or y1 >= w:
            continue
        j = x1*w+y1
        sj = s[x1][y1]
        if sj == '.':
            links[i].append(j)
        elif arrow[cnt] == sj:
            links[i].append(j)

stack = [(r-1)*w+c-1]
ans[r-1][c-1] = 'o'
while stack:
    i = stack.pop()
    for j in links[i]:
        x = j//w
        y = j%w
        if ans[x][y] != 'x':
            continue
        ans[x][y] = 'o'
        stack.append(j)

print('\n'.join(map(lambda x: ''.join(x),ans)))
# print(links)


