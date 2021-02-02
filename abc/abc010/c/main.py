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

txa,tya,txb,tyb,T,V,n,*xy = map(int,read().split())
e = -0.000000001

it = iter(xy)
for x,y in zip(it,it):
    tmp = ((x-txa)**2 + (y-tya)**2)**0.5 + ((x-txb)**2 + (y-tyb)**2)**0.5
    if( T*V - tmp > e ):
        print('YES')
        exit()
print('NO')
