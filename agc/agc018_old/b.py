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

n,m = map(int,input().split())
a = tuple([tuple(map(int,input().split())) for _ in range(n)])

ok = n
ng = 0
for _ in range(10):
    mid = (ok+ng)//2

    check = True
    inds = [0] * n
    done = [0] * (m+1)
    while(check):
        cnt_max = 0
        cnt = [0] * (m+1)
        for i in range(n):
            ind = inds[i]
            while(done[a[i][ind]] != 0):
                ind += 1
                if(ind == m):
                    check = False
                    break
            if(ind < m):
                inds[i] = ind
                cnt[a[i][ind]] += 1
                cnt_max = max(cnt_max, cnt[a[i][ind]])

        if(cnt_max <= mid):
            break

        for i in range(1,m+1):
            if(cnt[i] > mid):
                done[i] = 1

    if(check):
        ok = mid
    else:
        ng = mid

print(ok)




'''

x人でいけるか、をチェックしたい
前からチェックしていってx回以上出る数を捨てていけばよい？

いけそうだけどデータ構造がむずい

データを作る　O(N)
カウントする　O(N)
overしたやつを次に置き換える　O(N)

いけそうじゃない？

'''
