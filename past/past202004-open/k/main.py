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
s = input()
c = list(map(int,input().split()))
d = list(map(int,input().split()))

inf = 10**15
n2 = n//2 + 2
dp = [[inf] * n2 for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    ci = c[i]
    di = d[i]
    if(s[i] == '('):
        for j in range(n2):
            if(j != 0):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-1])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + di)
            if(j != n2-1):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j+1] + ci)
    else:
        for j in range(n2):
            if(j != n2-1):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j+1])
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + di)
            if(j != 0):
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-1] + ci)

print(dp[-1][0])


'''
dp[i][j] := i文字目まで見て、(がj個多いときの最小コスト

・s[i] == '('のとき
残す
消す
変える

・s[i] == ')'のとき
残す
消す
変える

'''