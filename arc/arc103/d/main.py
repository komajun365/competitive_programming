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

n,*xy = map(int,read().split())

parity  = (xy[0] + xy[1]) % 2
m = 32 - parity
d = [1 << max(x,0) for x in range(30,-2+parity,-1)  ]

w = []
it = iter(xy)
for x,y in zip(it,it):
    if (x+y)% 2 != parity:
        print(-1)
        exit() 
    i,j = 0,0
    res = ''
    for di in d:
        dx = x-i
        dy = y-j
        if dx >= abs(dy):
            res += 'R'
            i += di
        elif -dx >= abs(dy):
            res += 'L'
            i -= di
        elif dy >= 0:
            res += 'U'
            j += di
        else:
            res += 'D'
            j -= di
    w.append(res[::])

    # print(x,y,i,j)

print(m)
print(' '.join(map(str,d)))
print('\n'.join(w))
