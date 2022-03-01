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
read = sys.stdin.buffer.read

h,w,n,*ab = map(int,read().split())

aa = set()
bb = set()
it = iter(ab)
for ai,bi in zip(it,it):
    aa.add(ai)
    bb.add(bi)

aa = list(aa)
aa.sort()
bb = list(bb)
bb.sort()

encode_a = dict()
encode_b = dict()
for i,ai in enumerate(aa,1):
    encode_a[ai] = i
for i,bi in enumerate(bb,1):
    encode_b[bi] = i

ans = []
it = iter(ab)
for ai,bi in zip(it,it):
    ans.append('{} {}'.format(encode_a[ai], encode_b[bi]))
print('\n'.join(ans))