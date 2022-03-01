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

x,k,*data = map(int,read().split())

r = [0] + data[:k]
q = data[k]
ta = data[k+1:]

idx = 0
ans = []
lr = [[0,0],[x,x]] #[ai,now]

for i in range(q):
    t,a = ta[i*2:i*2+2]
    
    while idx < k:
        if r[idx+1] > t:
            break
    
        d = r[idx+1] - r[idx]
        if lr[0][0] == -1:
            if idx % 2 == 0:
                # down
                lr[0][1] = max(0,lr[0][1]-d)
                lr[1][1] = max(0,lr[1][1]-d)
            else:
                # up
                lr[0][1] = min(x,lr[0][1]+d)
                lr[1][1] = min(x,lr[1][1]+d)
            idx += 1
            continue

        # lr2 = [[0,0], [0,0]]
        if idx % 2 == 0:
            # down
            lr[0][1] = lr[0][1] - d
            lr[1][1] = lr[1][1] - d

            if lr[1][1] <= 0:
                lr = [[-1,0],[-1,0]]
            elif lr[0][1] <= 0:
                lr[0][0] -= lr[0][1]
                lr[0][1] = 0
        else:
            # up
            lr[0][1] = lr[0][1] + d
            lr[1][1] = lr[1][1] + d

            if lr[0][1] >= x:
                lr = [[-1,x],[-1,x]]
            elif lr[1][1] >= x:
                lr[1][0] -= lr[1][1] - x
                lr[1][1] = x
        idx += 1
    
    d = t - r[idx]
    if lr[0][0] == -1:
        tmp = lr[0][1]
    elif a <= lr[0][0]:
        tmp = lr[0][1]
    elif a >= lr[1][0]:
        tmp = lr[1][1]
    else:
        tmp = lr[0][1] + a - lr[0][0]

    if idx % 2 == 0:
        # down
        tmp = max(0,tmp-d)
    else:
        # up
        tmp = min(x,tmp+d)
    
    ans.append(tmp)

print('\n'.join(map(str,ans)))







            







'''
入力例３
100
5
48 141 231 314 425
7
0 19
50 98
143 30
231 55
342 0
365 100
600 10

t=0 
ai = 100-0 : 100-0

t=48
ai = 100-48 : 52-0

t=141
ai = 55-48 : 100-93

t=231
ai = 55-48 : 10-3

t=314
ai = 55-48 : 93-86

t=425
ai = xx : 0

19
52
91
10
58
42
100

'''