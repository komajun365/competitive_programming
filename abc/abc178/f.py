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

# from heapq import heappop,heappush

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

cnt = [[0,i] for i in range(n+1)]
cnt_a = [0] * (n+1)
cnt_b = [0] * (n+1)

for ai,bi in zip(a,b):
    cnt[ai][0] += 1
    cnt[bi][0] += 1
    cnt_a[ai] += 1
    cnt_b[bi] += 1

cnt.sort(reverse=True)
new_al = []
new_ar = []
new_bl = []
new_br = []
done = 0
for _,i in cnt:
    if(done >= n):
        new_ar += [i] * cnt_a[i]
        new_bl += [i] * cnt_b[i]
    elif(done + cnt_a[i] + cnt_b[i] <= n):
        new_al += [i] * cnt_a[i]
        new_br += [i] * cnt_b[i]
    else:
        if(cnt_a[i] > n-done):
            new_al += [i] * (n-done)
            new_ar += [i] * (cnt_a[i] - n + done)
            new_bl += [i] * cnt_b[i]
        else:
            new_al += [i] * cnt_a[i]
            new_br += [i] * (n - done - cnt_a[i])
            new_bl += [i] * (cnt_b[i] - (n - done - cnt_a[i]))
    done += cnt_a[i] + cnt_b[i]


new_a = new_al + new_ar[::-1]
new_b = new_bl + new_br[::-1]
new = [[ai,bi] for ai,bi in zip(new_a,new_b)]


new.sort()

ans =[]
for ni in new:
    x,y = ni
    if(x==y):
        print('No')
        exit()
    ans.append(y)

print('Yes')
print(' '.join(map(str,ans)))
