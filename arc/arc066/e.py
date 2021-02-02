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

n = int(input())
a = input().split()
if(n==1):
    print(a[0])
    exit()

a_num = list( map(int, a[::2]))
a_op = a[1::2]

cumsum = a_num[::]
cumsum_op = [0] * n
cumsum_op[0] = a_num[0]
minus_ind = []
for i in range(1,n):
    cumsum[i] += cumsum[i-1]
    if(a_op[i-1] == '+'):
        cumsum_op[i] = cumsum_op[i-1] + a_num[i]
    else:
        cumsum_op[i] = cumsum_op[i-1] - a_num[i]
        minus_ind.append(i)

ans = cumsum_op[-1]
if(len(minus_ind)<2):
    print(ans)
    exit()

for l,r in zip(minus_ind[:-1],minus_ind[1:]):
    # lまでは符号通り、l,r-1までを減算、r以降を全て加算
    tmp = cumsum_op[l-1] - (cumsum[r-1] - cumsum[l-1]) + (cumsum[-1] - cumsum[r-1])
    ans = max(ans,tmp)

print(ans)

# print(cumsum)
# print(cumsum_op)
# print(minus_ind)
