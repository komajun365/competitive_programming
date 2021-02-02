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
ans = 0
for i in range(1,n+1):
    x = i
    ch = 1
    while(x > 0):
        if(x%10)==7:
            ch = 0
            break
        x //= 10
    x = i
    while(x > 0):
        if(x%8)==7:
            ch = 0
            break
        x //= 8
    ans += ch
print(ans)
