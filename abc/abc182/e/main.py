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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

h,w,n,m,*data = map(int,read().split())

ab = data[:2*n]
cd = data[2*n:]

light_x = [[w+2] for _ in range(h+2)]
light_y = [[h+2] for _ in range(w+2)]
block_x = [[w+1] for _ in range(h+2)]
block_y = [[h+1] for _ in range(w+2)]

it = iter(ab)
for a,b in zip(it,it):
    light_x[a].append(b)
    light_y[b].append(a)

it = iter(cd)
for c,d in zip(it,it):
    block_x[c].append(d)
    block_y[d].append(c)

field = [[0] * (w+2) for _ in range(h+2)]

# x
for i in range(1,h+1):
    light = sorted(light_x[i])
    block = sorted(block_x[i])
    li = 0
    bi = 0
    l = 0
    while(l < w+1):
        r = block[bi]
        flag = 0
        while(light[li] < w+2):
            if(light[li] < r):
                flag = 1
                li += 1
            else:
                break
        for j in range(l+1, r):
            field[i][j] |= flag
        l = r
        bi += 1

# y
for j in range(1,w+1):
    light = sorted(light_y[j])
    block = sorted(block_y[j])
    li = 0
    bi = 0
    l = 0
    while(l < h+1):
        r = block[bi]
        flag = 0
        while(light[li] < h+2):
            if(light[li] < r):
                flag = 1
                li += 1
            else:
                break
        for i in range(l+1, r):
            field[i][j] |= flag
        l = r
        bi += 1

ans = 0
for fi in field:
    ans += sum(fi)
print(ans)