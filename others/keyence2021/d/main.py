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
if n==1:
    print(1)
    print('AB')
    exit()
elif n == 2:
    print(3)
    print('AABB')
    print('ABAB')
    print('ABBA')
    exit()

table = [[0,0,0],[0,1,1],[1,0,1],[1,1,0]]

for i in range(2,n):
    m = 2**(i+1)
    next = [[0] * (m-1) for _ in range(m)]

    w = len(table[0])
    h = len(table)
    for j in range(h*2):
        for k in range(w):
            next[j][k] = table[j//2][k]
        next[j][w] = j%2
        for k in range(w):
            next[j][k+w+1] = next[j][k] ^ next[j][w]
    
    table, next = next,table

print(2**n-1)
for i in range(1,2**n):
    tmp = 'A'
    for j in table[i]:
        if j == 0:
            tmp += 'A'
        else:
            tmp += 'B'
    print(tmp)

