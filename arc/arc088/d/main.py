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
l = len(s)
ans = 0
if l % 2== 0:
    left = s[:l//2]
    right = s[l//2:]
    ans = l//2
    p = left[-1]
else:
    left = s[:l//2]
    right = s[l//2+1:]
    ans = l//2 + 1
    p = s[l//2]


for i in range(l//2):
    if left[-i-1] != p or right[i] != p:
        break
    ans += 1
print(ans)
