# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
input = sys.stdin.readline
# キュー
from collections import deque


n = int(input())
m = int(input())

win = [0] * (n+1)
up =  [set() for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    up[b].add(a)
    win[a] += 1

deqs = [deque(), deque()]
ranks = {}
tmp = 0
for i,val in enumerate(win[1:],1):
    if(val==0):
        deqs[tmp%2].append(i)

remain = set(range(1,n+1))
while(True):
    ranks[tmp] = []
    while(deqs[tmp%2]):
        loser = deqs[tmp%2].pop()
        ranks[tmp].append(loser)
        remain.remove(loser)
        for winner in up[loser]:
            win[winner] -= 1
            if(win[winner] == 0):
                deqs[(tmp+1)%2].append(winner)
    tmp += 1
    if(not deqs[tmp%2]):
        break

for i in range(tmp):
    print('\n'.join(map(str,ranks[tmp-1-i])))
if(remain):
    print('\n'.join(map(str,list(remain))))
print(1*(tmp!=n))
