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
from collections import defaultdict
import bisect

n,m,k = map(int,readline().split())
s = read().split()

follow = defaultdict(int)
tweet = [[] for _ in range(n+1)]
cnt = [0] * (n+1)

ind = 0
while(ind < len(s)):
    if(s[ind] == 't'):
        i = int(s[ind+1])
        tweet[i].append(ind)
        ind += 2
    elif(s[ind] == 'f'):
        i = int(s[ind+1])
        j = int(s[ind+2])
        if(j<i):
            i,j = j,i
        follow[i*(n+1)+j] = ind
        ind += 3
    else:
        i = int(s[ind+1])
        j = int(s[ind+2])
        if(j<i):
            i,j = j,i
        f_ind = follow.pop(i*(n+1)+j)
        i_tweet = len(tweet[i]) - bisect.bisect_left(tweet[i], f_ind)
        j_tweet = len(tweet[j]) - bisect.bisect_left(tweet[j], f_ind)
        cnt[i] += j_tweet
        cnt[j] += i_tweet
        ind += 3

for key,val in follow.items():
    i = key//(n+1)
    j = key%(n+1)
    i_tweet = len(tweet[i]) - bisect.bisect_left(tweet[i], val)
    j_tweet = len(tweet[j]) - bisect.bisect_left(tweet[j], val)
    cnt[i] += j_tweet
    cnt[j] += i_tweet

for i in range(1,n+1):
    cnt[i] += len(tweet[i])

cnt.sort(reverse=True)
print(cnt[k-1])




'''
ふぉろー、アンフォローの時にまとめて計算すればよい。
あとは、最後に全員アンフォローしたとする。
'''
