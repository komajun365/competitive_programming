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

ans = 0
cnt = 0
for x in range(2,1000):
    tmp = 0
    for ai in a:
        if(ai%x == 0):
            tmp += 1
    
    if(cnt < tmp):
        cnt = tmp
        ans = x
print(ans)
