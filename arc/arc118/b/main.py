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

k,n,m = map(int,input().split())
a = list(map(int,input().split()))

b = []
dif = []

for i in range(k):
    ai = a[i]
    am = ai*m
    bi = am//n
    b.append(bi)
    dif.append([am-bi*n,i])

# print(' '.join(map(str,b)))

dif.sort(reverse=True)
up = m - sum(b)
for i in range(up):
    _, idx = dif[i]
    b[idx] += 1

print(' '.join(map(str,b)))