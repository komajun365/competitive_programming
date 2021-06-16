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

n,m = map(int,input().split())
a = list(map(int,input().split()))

idxs = [[-1] for _ in range(n)]
for i,ai in enumerate(a):
    idxs[ai].append(i)

for i in range(n):
    l = len(idxs[i])
    idxs[i].append(n)
    for j in range(l):
        dif = idxs[i][j+1] - idxs[i][j] - 1
        if dif >= m:
            print(i)
            exit()
print(n)