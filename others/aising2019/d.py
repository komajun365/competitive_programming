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
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
import bisect

n,q = map(int,readline().split())
a = [0] + list(map(int,readline().split()))
x = [0] + list(map(int,read().split()))

cumsum = [0] * (n+1)
cumsum_eo = [0] * (n+1)

for i in range(1,n+1):
    cumsum[i] = cumsum[i-1] + a[i]
    if(i==1):
        cumsum_eo[1] = a[1]
    else:
        cumsum_eo[i] = cumsum_eo[i-2] + a[i]

ans = []
for xi in x[1:]:
    ok = 0
    ng = (n+4)//2
    cnt=0
    while(ng-ok > 1):
        mid = (ng+ok)//2
        if( mid*2-1 > n):
            ng = mid
            continue

        t_l = a[n+1-mid]
        a_r = a[n-mid]
        a_lr = a[n+1-mid*2+1]

        if(t_l - xi < xi-a_lr ):
            ng = mid
        else:
            ok = mid

        cnt+=1

    t_l_ind = n+1-ok
    a_l_ind = n+1-ok*2

    tmp = cumsum[-1] - cumsum[t_l_ind-1]
    if(a_l_ind>1):
        tmp += cumsum_eo[a_l_ind-1]
    ans.append(tmp)
    # print(ng,ok)

print('\n'.join(map(str,ans)))
