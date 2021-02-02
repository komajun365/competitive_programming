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

n,m,y,z = map(int,input().split())
d = dict()
p = []
for i in range(m):
    ci,pi = input().split()
    pi = int(pi)
    d[ci] = i
    p.append(pi)

b0 = input()
b = []
for i,bi in enumerate(b0):
    b.append(d[bi])

if(m==1):
    ans0 = n*p[0] + (n-1)*y + z
    ans1 = p[0] + z
    print(max(ans0,ans1,0))
    exit()

inf = -1 * 10**9
dp = [[inf] * (2**m) for _ in range(m)]
for i in range(m):
    dp[i][0] = 0
done = [0] * m
for i,bi in enumerate(b):
    add = p[bi] + y
    if(add > 0):
        for j in range(2**m):
            if(j >> bi)&1:
                dp[bi][j] += add
    for c in range(m):
        if(bi!=c):
            for j in range(2**m):
                dp[bi][j | (1<<bi)] = max(dp[bi][j | (1<<bi)],dp[c][j]+p[bi])
    
    # print(bi)
    # print(dp)

ans = 0
for i in range(m):
    ans = max(ans, max(dp[i][:-1]))
    ans = max(ans, dp[i][-1] + z)

print(ans)
# print(dp)




'''
最後に使った色
今まで使った色
どこまで見たか

dp[i][j][k]:=
iの色を使っていて
最後にjの色を使っていて
k番目のブロックを処理したときの最高点数
i = 2**10
j = 10
k = 5*10**3

5*10**7


'''