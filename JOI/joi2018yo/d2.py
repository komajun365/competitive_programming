# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討24分　実装9分 バグとり15分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
L = list(map(int,read().split()))
cumsum = [0] * (N+1)
for i in range(N):
    cumsum[i+1] += cumsum[i] + L[i]

if(N==2):
    print(abs(L[1]-L[0]))
    exit()

l_mins = set()
for i in range(N):
    for j in range(i+1,N+1):
        tmp = cumsum[j]-cumsum[i]
        if(tmp <= cumsum[-1]//2):
            l_mins.add(tmp)


ans = 1000
for l_min in l_mins:
    OK = 1000
    NG = -1
    for _ in range(12):
        mid = (OK+NG)//2
        can_cut=1
        for i in range(N):
            if not ((can_cut >> i) & 1):
                continue
            for j in range(i+1,N+1):
                new = cumsum[j]-cumsum[i]
                if(new < l_min):
                    continue
                if(new > l_min+mid):
                    break
                can_cut = can_cut | (1<<j)
        if((can_cut>>N) & 1):
            OK = mid
        else:
            NG = mid

    ans = min(ans,OK)

print(ans)



'''
最小ピースの長さをl_min,最大ピースの長さをl_min+midと仮定する。
can_cut[i] := i番目の切れ目でカットするとき、全てのピースをl_min~l_maxの間に収めることができるか
で管理するとする。

can_cutの更新は下記で実施。
for j in range(1,i-1):
    if(can_cut[j]==True)&(l_min <= cumsum[i]-cumsum[j] <= l_min+mid):
        can_cut[i]==True
※実装はbit演算で対応した

l_minは1-(N*500)の範囲を探索
→　と思ったが、ピースの長さは高々n**2//2通りなので、
　　それを探索範囲にすればよい
全部の切れ目で切ることを考えると、
midはmax(L)以下であることがわかるので、0-1000の範囲を二分探索すればよい。

can_cutを求めるのにO(N**2)
l_minの探索はO(N**2)
midはO(logL)
なので全体で
O(N**4logL) ≒O（6.25*10**7）
'''
