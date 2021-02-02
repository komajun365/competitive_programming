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

from heapq import heappop,heappush

n = int(input())
a = list(map(int,input().split()))
dic = dict()
for i,ai in enumerate(a,1):
    if(ai-1 in dic):
        print('No')
        eixt()
    dic[ai-1] = i

hq = []
for i,ai in enumerate(a[1:],2):
    heappush(hq,(ai-i,i-1,i))

others = []
ans = []
for ind in range(n**2):
    if ind in dic:
        i = dic[ind]
        ans.append(i)
        others += [i] * (n-i)
        continue

    if(hq):
        num,rem,i = heappop(hq)
        if(num < ind):
            print('No')
            exit()
        elif(rem==1):
            ans.append(i)
        else:
            ans.append(i)
            heappush(hq,(num+1,rem-1,i))
    else:
        if(others):
            ans.append(others.pop())
        else:
            print('No')
            exit()



print('Yes')
print(' '.join(map(str,ans)))


'''
1-n**2 で増加列をn個作る

？？？
厳しい奴からとってく、ではだめなのか？

'''
