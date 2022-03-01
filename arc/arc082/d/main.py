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
p = list(map(int,input().split()))

ans = 0
cnt = 0
for i,pi in enumerate(p,1):
    if i == pi:
        cnt += 1
    else:
        ans += (cnt+1)//2
        cnt = 0
else:
    ans += (cnt+1)//2
    cnt = 0
print(ans)

