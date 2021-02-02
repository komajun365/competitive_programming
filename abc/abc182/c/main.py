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

n = input()
cnt = [0,0,0]
for ni in n:
    ni = int(ni)
    cnt[ni%3] += 1

tot = cnt[1] * 1 + cnt[2] * 2
ans = -1
if(tot%3 == 0):
    ans = 0
elif(tot%3==1):
    if(cnt[1] >= 1):
        ans = 1
    elif(cnt[2] >= 2):
        ans = 2
else:
    if(cnt[2] >= 1):
        ans = 1
    elif(cnt[1] >= 2):
        ans = 2

if(ans == len(n)):
    ans = -1
print(ans)