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
if(n==2):
    print(-1)
    exit()

p3 = ['.aa','b..','b..']
p4 = ['aabc','ddbc','efgg','efhh']
p5 = ['aabbc','d.eec','df..g','hf..g','hiijj']
p6 = ['.aabbc','d..e.c','d..eff']
p7 = ['.aabbcc','a.ddee.','ad....d','bd....d','be....e','ce....e','c.ddee.']

for pi in p6[::]:
    p6.append(pi[::-1])

if(n==3):
    for pi in p3:
        print(pi)
    exit()
if(n==7):
    for pi in p7:
        print(pi)
    exit()

ans = [['.'] * n for _ in range(n)]
if(n%3==0):
    for k in range(0,n,3):
        for i in range(3):
            for j in range(3):
                ans[k+i][k+j] = p3[i][j]
else:
    cut = []
    x = n
    if(x%4==1):
        cut.append(5)
        x -= 5
    elif(x%4==2):
        cut.append(6)
        x -= 6
    elif(x%4==3):
        cut.append(5)
        cut.append(6)
        x -= 11
    cut += [4] * (x//4)

    idx = 0
    for ci in cut:
        if(ci == 4):
            p = p4
        elif(ci == 5):
            p = p5
        else:
            p = p6

        for i in range(ci):
            for j in range(ci):
                ans[idx+i][idx+j] = p[i][j]
        
        idx += ci

for ai in ans:
    print(''.join(ai))


