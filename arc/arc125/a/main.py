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

n,m = map(int,input().split())
s = list(map(int,input().split()))
t = list(map(int,input().split()))

if sum(s) == n and sum(t) != m:
    print(-1)
    exit()
elif sum(s) == 0 and sum(t) != 0:
    print(-1)
    exit()
elif s[0] == 0 and sum(t) == 0:
    print(m)
    exit()
elif s[0] == 1 and sum(t) == m:
    print(m)
    exit()

move = [0,0]
if t[0] == 0:
    move[1] = 1
else:
    move[0] = 1

for i in range(m-1):
    if t[i] != t[i+1]:
        move[0] += 1
        move[1] += 1

ans = 10**10
s2 = s + s
for i in range(n):
    if s2[i-1] == s2[i] == s2[i+1]:
        continue
    cand = move[s2[i]] + m + min(i, n-i)
    ans = min(ans, cand)

print(ans)