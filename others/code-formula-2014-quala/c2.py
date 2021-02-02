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

n,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

done = set()
done_ind = set()
lim = 0
for i in range(n):
    ans = []
    ind = 0
    while(ind < k):
        if(ind%n > i):
            ind += 1
            continue
        cand = a[ind%n][ind//n]
        if(cand in done)&(not ind in done_ind):
            k += 1
        elif(not cand in done):
            ans.append(cand)
            done.add(cand)
        done_ind.add(ind)
        ind += 1
    ans.sort()
    print(' '.join(map(str,ans)))
