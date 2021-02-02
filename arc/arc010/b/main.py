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
days = [[] for _ in range(13)]
for i in range(1,13):
    if(i==2):
        days[i] = [0]*29
    elif(i in [4,6,9,11]):
        days[i] = [0]*30
    else:
        days[i] = [0]*31

for _ in range(n):
    m,d = map(int,input().split('/'))
    days[m][d-1] = 1

ans = 0
tmp = 0
cnt = 1
carry = 0
for i in range(1,13):
    if(i==2):
        d = 29
    elif(i in [4,6,9,11]):
        d = 30
    else:
        d = 31

    for j in range(d):
        if(cnt%7 <= 1):
            days[i][j] += 1
        days[i][j] += carry
        carry = 0
        if(days[i][j] == 0):
            tmp = 0
        else:
            carry = days[i][j]-1
            tmp += 1
            ans = max(ans,tmp)
        cnt += 1

print(ans)
# print(days)