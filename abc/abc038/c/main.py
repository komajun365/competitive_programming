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
tmp = 1
b = a[0]
for i in range(1,n):
    if(b < a[i]):
        tmp += 1
    else:
        ans += (tmp * (tmp+1)) //2
        tmp = 1
    b = a[i]
ans += (tmp * (tmp+1)) //2
print(ans)
    