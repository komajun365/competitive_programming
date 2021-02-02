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

# unionするときどっちを根にするか指定できるようにした。
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self,x):
        if(self.parents[x] < 0):
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def size(self, x):
        return self.parents[ self.find(x) ] * -1

    def same(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        return (x_root == y_root)

    def union(self,x,y):
        x_root = self.find(x)
        y_root = self.find(y)
        if(x == y):
            return

        # 常にx側を根にする。
        self.parents[y_root] = x_root


    def members(self,x):
        root = self.find(x)
        ret = [ i for i in range(self.n) if self.find(i) == root ]
        return ret

    def roots(self):
        ret = [ i for i in range(self.n) if self.parents[i] < 0]
        return ret

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

N, X = map(int, input().split())
T = list(map(int, input().split()))
TM = max(T)
A = list(map(int, input().split()))

left = UnionFind(TM+1)

TA = [(t, a) for t, a in zip(T, A)]
TA.sort(key=lambda x:x[1], reverse=True)

ans = 0
score = 0
for t, a in TA:
    l = left.find(t)
    if(l==0):
        continue

    score += a
    ans += 1
    left.union(l-1,t)

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
