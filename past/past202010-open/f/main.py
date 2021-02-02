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
readline = sys.stdin.readline
readlines = sys.stdin.readlines

n,k = map(int,readline().split())
s = read().split()

d = dict()
for si in s:
    if(si in d):
        d[si] += 1
    else:
        d[si] = 1

cnt = []
for key,val in d.items():
    cnt.append([val,key])

cnt.sort(key=lambda x: x[0]*-1)
cnt.append([0,'inf'])
vb,_ = cnt[k-2]
vk,ans = cnt[k-1]
va,_ = cnt[k]
if(vb != vk != va):
    print(ans)
else:
    print('AMBIGUOUS')
# print(cnt)