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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heappop,heappush

class BIT():
    def __init__(self, max_n):
        self.size = max_n + 1
        self.tree = [0] * self.size

    def get_sum(self,i):
        s = 0
        while i:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i < self.size:
            self.tree[i] += x
            i += i & -i

n,q = map(int,readline().split())
c = list(map(int,readline().split()))
lr = list(map(int,read().split()))
it = iter(lr)
hq = []
for i,l,r in zip(range(q),it,it):
    heappush(hq, (r-1,l-1,i))

st = BIT(n+1)
ans = [0] * q
before = [-1] * (n+1)
c_ind = 0
while(hq):
    r,l,i = heappop(hq)
    while(c_ind <= r):
        bef = before[c[c_ind]]
        if(bef!=-1):
            st.add(bef+1,-1)
        before[c[c_ind]] = c_ind
        c_ind += 1

    ans[i] = r-l+1 + st.get_sum(r+1) - st.get_sum(l)

print('\n'.join(map(str,ans)))
