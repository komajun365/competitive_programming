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

import sys
read = sys.stdin.read

n,m,q,*data = map(int,read().split())
xy = data[:2*m]
ab = data[2*m:]

links = [[] for _ in range(n)]
it = iter(xy)
for x,y in zip(it,it):
  x -= 1
  y -= 1
  links[x].append(y)

dp = []
for i in range(n):
  dp.append(1<<i)

for i in range(n):
  for j in links[i]:
    dp[j] |= dp[i]

ans = []
it = iter(ab)
for a,b in zip(it,it):
  a -= 1
  b -= 1
  if (dp[b] >> a) & 1:
    ans.append('Yes')
  else:
    ans.append('No')

print('\n'.join(ans))