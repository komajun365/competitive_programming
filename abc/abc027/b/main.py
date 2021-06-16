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
a = list(map(int,input().split()))

tot = sum(a)
if tot % n != 0:
    print(-1)
    exit()
p = tot//n

ans = 0
tmp = 0
for i in range(n-1):
    tmp += a[i] - p
    if tmp != 0:
        ans += 1
print(ans)