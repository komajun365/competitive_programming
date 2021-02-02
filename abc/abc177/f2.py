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

h,w = map(int,readline().split())
data = list(map(int,read().split()))

# N: 処理する区間の長さ
N = w+2

INF = 10**15

LV = (N-1).bit_length()
N0 = 2**LV
data = [INF]*(2*N0)

# print(LV)
# print(N0)
# print(data)

for i,num in zip(range(N0+1,N0+w+1),range(w-1,-1,-1)):
    data[i] = num*10**7
# print(data)
for i in range(N0-2,-1,-1):
    data[i] = min(data[i*2+1], data[i*2+2])

lazy = [None]*(2*N0)

# 伝搬対象の区間を求める
def gindex(l, r):
    L = (l + N0) >> 1; R = (r + N0) >> 1
    lc = 0 if l & 1 else (L & -L).bit_length()
    rc = 0 if r & 1 else (R & -R).bit_length()
    for i in range(LV):
        if rc <= i:
            yield R
        if L < R and lc <= i:
            yield L
        L >>= 1; R >>= 1

# 遅延伝搬処理
def propagates(*ids):
    for i in reversed(ids):
        v = lazy[i-1]
        if v is None:
            continue
        lazy[2*i-1] = data[2*i-1] = lazy[2*i] = data[2*i] = v
        lazy[i-1] = None

# 区間[l, r)をxで更新
def update(l, r, x):
    *ids, = gindex(l, r)
    propagates(*ids)

    L = N0 + l; R = N0 + r
    while L < R:
        if R & 1:
            R -= 1
            lazy[R-1] = data[R-1] = x
        if L & 1:
            lazy[L-1] = data[L-1] = x
            L += 1
        L >>= 1; R >>= 1
    for i in ids:
        data[i-1] = min(data[2*i-1], data[2*i])

# 区間[l, r)内の最小値を求める
def query(l, r):
    propagates(*gindex(l, r))
    L = N0 + l; R = N0 + r

    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])
        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s

# print(data)


ans = []

it = iter(data)
for i,a,b in zip(range(1,h+1), it,it):
    update(a,b+1, INF)
    tmp = query(a,b+2)
    update(b+1,b+2, tmp - (w-b-1))
    tmp = query(1,w+1)
    ans.append()

print('\n'.join(map(str,ans)))
