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

n,a,b = map(int,input().split())
p = list(map(int,input().split()))

idx = [-1] * (n+1)
for i,pi in enumerate(p,1):
    idx[pi] = i

inf = 10**14
dp = [inf] * (n+1)
dp[0] = 0
done = [0] * (n+1)

for i in range(1,n+1):
    next = [inf] * (n+1)
    for j in range(n+1):
        if(idx[i] <= j):
            next[j] = min(next[j], dp[j])
        else:
            next[j] = min(next[j], dp[j] + b)
            tmp = idx[i] - 1 - j - (done[idx[i]] - done[j])
            next[idx[i]] = min(next[idx[i]], dp[j] + a*tmp)
    dp,next = next,dp

    for j in range(idx[i],n+1):
        done[j] += 1

ans = min(dp)
print(ans)




