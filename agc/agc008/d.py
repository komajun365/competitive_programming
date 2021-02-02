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

hq = []
for i,ai in enumerate(a):
    # heappush(hq,(ai-i,i,i))
    heappush(hq,((ai-i-1)*n - i,i+1))

others = []

ans = []
for ind in range(n**2):
    print(ind,ans)
    print(hq)
    print(others)
    if(hq):
        num,i = heappop(hq)
        rem = (-1*num)%n
        num = (num+rem)//n
        print(num,rem,i)
        if(num < ind):
            print('No')
            exit()
        elif(num==ind)&(rem==0):
            ans.append(i)
            others += [i] * (n-i)
        elif(rem==0):
            if(others):
                ans.append(others.pop())
                heappush(hq,(num*n-rem,i))
            else:
                print('No')
                exit()
        else:
            ans.append(i)
            heappush(hq,((num+1)*n - (rem-1),i))
            # heappush(hq,(num+1,rem-1,i))
    else:
        ans.append(others.pop())


print('Yes')
print(' '.join(map(str,ans)))


'''
1-n**2 で増加列をn個作る

？？？
厳しい奴からとってく、ではだめなのか？

'''
