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

n,x = map(int,input().split())
a = list(map(int,input().split()))

ans = x
inf = -1 * 10**10
for k in range(1,n+1):
    dp = [[inf]*k for _ in range(k+1)]
    dp[0][0] = 0
    for i in range(n):
        ai = a[i]
        m = ai % k
        for xi in range(k-1,-1,-1):
            for yi in range(k):
                if dp[xi][yi] == inf:
                    continue
                dp[xi+1][(yi+m)%k] = max(dp[xi+1][(yi+m)%k], dp[xi][yi]+ai)
    
    mp = dp[-1][x%k]
    # print(k)
    # for tmp in dp:
    #     print(tmp)

    if mp == inf:
        continue
    ans = min(ans, (x-mp)//k)

print(ans)



