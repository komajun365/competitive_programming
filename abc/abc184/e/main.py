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
readline = sys.stdin.readline
readlines = sys.stdin.readlines

h,w = map(int,readline().split())
a = read().split()

inf = 10**6
dp = [[inf] * w for _ in range(h)]

s = -1
g = -1
tele = dict()
for i in range(h):
    for j in range(w):
        if(a[i][j] == 'S'):
            dp[i][j] = 0
            s = i*10000+j
        elif(a[i][j] == 'G'):
            g = i*10000+j
        elif(a[i][j] == '.'):
            continue
        elif(a[i][j] == '#'):
            dp[i][j] = -1
        else:
            alp = a[i][j]
            if(alp in tele):
                tele[alp].append([i,j])
            else:
                tele[alp] = [[i,j]]

# move = dict()
# for key,val in tele.items():
#     i0,j0 = val[0]
#     i1,j1 = val[1]
#     move[i0*10000+j0] = [i1,j1]
#     move[i1*10000+j1] = [i0,j0]


done = set()
stack = [s]
while(stack):
    bef = []
    stack,bef = bef,stack
    while(bef):
        num = bef.pop()
        i = num // 10000
        j = num % 10000
        for dx,dy in zip([-1,0,1,0], [0,-1,0,1]):
            dx += i
            dy += j
            if(dx < 0) or (dx >= h) or (dy < 0) or (dy >= w):
                continue
            if(dp[dx][dy] != inf):
                continue
            if(a[dx][dy] == 'S'):
                continue
            elif(a[dx][dy] == 'G'):
                print(dp[i][j] + 1)
                exit()               
            elif(a[dx][dy] == '#'):
                continue
            else:
                dp[dx][dy] = dp[i][j] + 1
                stack.append(dx*10000+dy)
        if(not a[i][j] in 'SG.#'):
            if(a[i][j] in done):
                continue
            done.add(a[i][j])
            for wi,wj in tele[a[i][j]]:
                if(dp[wi][wj] != inf):
                    continue
                dp[wi][wj] = dp[i][j] + 1
                stack.append(wi*10000+wj)

print(-1)
# print(dp)