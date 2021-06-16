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
a,b,c = map(int,input().split())

ans = 9999
for i in range(10000):
    if i*a > n:
        break
    for j in range(10000-i):
        tot = i*a+j*b
        if tot > n:
            break
        rem = n-tot
        if rem % c == 0:
            k = rem//c
            ans = min(ans, i+j+k)
print(ans)
