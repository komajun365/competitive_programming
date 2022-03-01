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

l = 0
now = 1
nums = []
while now < n:
    if s[now] != s[now-1]:
        nums.append(now-l)
        l = now
    now += 1
else:
    nums.append(now-l)

ans = n*(n+1)//2
for x in nums:
    ans -= x*(x+1)//2
print(ans)