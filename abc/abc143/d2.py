import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
l = list(map(int,input().split()))

l.sort()

ans = 0
for i in range(n-2):
    l1 = l[i]

    l3_ind = i+2
    for j in range(i+1,n):
        l2 = l[j]
        while(True):
            if(l3_ind == n):
                ans += l3_ind - j - 1
                break

            if(l[l3_ind] >= l1+l2):
                ans += l3_ind - j - 1
                break
            l3_ind += 1

print(ans)
