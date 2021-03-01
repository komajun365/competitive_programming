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
s1 = input()
s2 = input()
mod = 1000000007

dmn = []
idx = 0
while(idx < n):
    if s1[idx] == s2[idx]:
        dmn.append(1)
        idx += 1
    else:
        dmn.append(2)
        idx += 2

l = len(dmn)
if dmn[0] == 1:
    ans = 3
else:
    ans = 6
for i in range(l-1):
    a,b = dmn[i:i+2]
    if a == b == 1:
        ans *= 2
    elif a == 1 and b == 2:
        ans *= 2
    elif a == 2 and b == 1:
        ans *= 1
    else:
        ans *= 3
    ans %= mod
print(ans)