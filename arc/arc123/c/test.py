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

# import sys
# read = sys.stdin.buffer.read

# t,*case = map(int,read().split())

n = 10000
dp = [-1] * n
dp[0] = 0
stack = [0]
go = []
for i in range(1,n):
    x = i
    while x > 0:
        if 1 <= x <= 3:
            go.append(i)
            break
        elif 1 <= x % 10 <= 3:
            x //= 10
        else:
            break

# print(go)   

while stack:
    stack2 = []
    while stack:
        i = stack.pop()
        for gi in go:
            j = i + gi
            if j >= n:
                continue
            if dp[j] != -1:
                continue
            dp[j] = dp[i] + 1
            stack2.append(j)
    stack,stack2 = stack2,stack

def calc(x):
    for res in range(1,5):    
        s = str(x)
        l = len(s)
        dp = [[0,0] for _ in range(res+1)]
        for i in range(res+1):
            dp[i][0] = 1
        
        for i in range(l):
            si = int(s[i])
            dp2 = [[0,0] for _ in range(res+1)]
            for j in range(1,res+1):
                for k in range(j,res+1):
                    if dp[j][0] == 1:
                        if k <= si <= k*3:
                            dp2[k][0] = 1
                        if k <= si+1 <= k*3:
                            dp2[k][1] = 1
                    if dp[j][1] == 1:
                        if k <= si+10 <= k*3:
                            dp2[k][0] = 1
                        if k <= si+11 <= k*3:
                            dp2[k][1] = 1
            dp,dp2 = dp2,dp
        for i in range(1,res+1):
            if dp[i][0] == 1:
                return res

    return 5

for i in range(1,n):
    res = calc(i)
    if res != dp[i]:
        print(i, res,dp[i])


# for i in range(n):
#     if dp[i] == 5:
#         print(i)

