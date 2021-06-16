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

ans = []
for fx in range(1,200):
    x = n-fx
    tmp = 0
    while x > 0:
        tmp += x%10
        x //= 10
    if tmp == fx:
        ans.append(n-fx)
print(len(ans))
ans.sort()
for i in ans:
    print(i)