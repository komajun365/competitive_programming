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
for i in range(n):
    ans = []
    add = 0
    ind = 0
    while(ind < k):
        cand = a[i][ind//n]
        if( cand in done):
            add += 1
        else:
            ans.append(cand)
            done.add(cand)
        ind += n

    k += add
    while(ind < k):
        if(ind % n > )
        cand = a[ind%][ind//n]
        if( cand in done):
            add += 1
        else:
            ans.append(cand)
            done.add(cand)
        ind += 1
    ans.sort()
    print(' '.join(map(str,ans)))
