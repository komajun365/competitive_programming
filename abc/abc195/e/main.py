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
t = input()

can_go = [[-1] * 10 for _ in range(7)]
for i in range(7):
    for j in range(10):
        can_go[i][j] = [i * 10 % 7, (i * 10 + j) % 7]

rev = [set() for _ in range(70)]
for i in range(7):
    for j in range(10):
        for k in range(2):
            after = can_go[i][j][k]
            rev[after*10 + j].add(i)


def calc_tak(dp,si):
    res = [0] * 7
    for i in range(7):
        if dp[i] == 0:
            continue
        for j in rev[i*10+si]:
            res[j] = 1
    return res

def calc_ao(dp,si):
    res = [0] * 7
    for i in range(7):
        if dp[can_go[i][si][0]] == 1 and dp[can_go[i][si][1]] == 1:
            res[i] = 1
    return res

dp = [0] * 7
dp[0] = 1
for i in range(n-1,-1,-1):
    si = int(s[i])
    if t[i] == 'T':
        res = calc_tak(dp,si)
    else:
        res = calc_ao(dp,si)
    dp,res = res,dp

if dp[0] == 1:
    print('Takahashi')
else:
    print('Aoki')

