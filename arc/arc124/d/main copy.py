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
p = list(map(lambda x: int(x) - 1,input().split()))

ans = 0
use = [0] * (n+m)
for i in range(n+m):
    if use[i] == 1:
        continue
    if p[i] == i:
        use[i] = 1
        continue
    left = 0
    right = 0
    same_side = 0
    now = i
    go = p[i]
    while go != i:
        if now < n:
            left += 1
        else:
            right += 1
        if (now < n) ^ (go < n) == 0:
            same_side += 1
        use[now] = 1
        now = go
        go = p[now]
    else:
        if now < n:
            left += 1
        else:
            right += 1
        if (now < n) ^ (go < n) == 0:
            same_side += 1
        use[now] = 1
    
    if left == 0 or right == 0:
        ans += left + right + 1
    else:
        ans += (left + right - 1)
    # print(i,left,right,same_side)
    # print(use)

print(ans) 

        
