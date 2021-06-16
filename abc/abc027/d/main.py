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

s = input()
n = len(s)
pm = []
cnt_p = 0
cnt_m = 0
for i in range(n-1,-1,-1):
    if s[i] == '+':
        cnt_p += 1
    elif s[i] == '-':
        cnt_m += 1
    else:
        pm.append(cnt_p - cnt_m)

pm.sort()
l = len(pm)
ans = -1 * sum(pm[:l//2]) + sum(pm[l//2:])
print(ans)