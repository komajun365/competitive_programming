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

n,m,*ab = map(int,read().split())

links = [set() for _ in range(n+1)]
it=iter(ab)
for a,b in zip(it,it):
    links[a].add(b)

for i in links[1]:
    if(n in links[i]):
        print('POSSIBLE')
        exit()

print('IMPOSSIBLE')
