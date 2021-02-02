# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

N, X = map(int, input().split())
T = list(map(int, input().split()))
TM = max(T)
A = list(map(int, input().split()))
left = [i-1 for i in range(TM+1)]
right = [i+1 for i in range(TM+1)]
TA = [(t, a) for t, a in zip(T, A)]
TA.sort(key=lambda x:x[1], reverse=True)
used = [False] * (TM+1)
ans = 0
score = 0
for t, a in TA:
  t -= 1
  if not used[t]:
    used[t] = True
    score += a
    ans += 1
    l, r = left[t], right[t]
    left[r], right[l] = l, r
  elif left[t] >= 0:
    l = left[t]
    used[l] = True
    score += a
    ans += 1
    ll, rr = left[l], right[l]
    left[rr], right[ll] = ll, rr
    left[t],right[t] = ll, rr
  print(t,a)
  print(used)
  print(left)
  print(right)

  if score >= X:
    print(ans)
    quit()

print(-1)


# N, X = map(int, input().split())
# T = list(map(int, input().split()))
# TM = max(T)
# A = list(map(int, input().split()))
# left = [i-1 for i in range(TM+1)]
# right = [i+1 for i in range(TM+1)]
# TA = [(t, a) for t, a in zip(T, A)]
# TA.sort(key=lambda x:x[1], reverse=True)
# used = [False] * (TM+1)
# ans = 0
# score = 0
# for t, a in TA:
#   t -= 1
#   if not used[t]:
#     used[t] = True
#     score += a
#     ans += 1
#     l, r = left[t], right[t]
#     left[r], right[l] = l, r
#   elif left[t] >= 0:
#     l = left[t]
#     used[l] = True
#     score += a
#     ans += 1
#     ll, rr = left[l], right[l]
#     left[rr], right[ll] = ll, rr
#
#   if score >= X:
#     print(ans)
#     quit()
#
# print(-1)
