# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
p = list(map(int,input().split()))
p_ind = [ (p[i], i+1) for i in range(n) ]
p_ind.sort(reverse=True)

# 平方分割します。
max_n = 10**5
div_n = int(max_n**(1/2))+1
a = [[] for _ in range(div_n)]
a[0] = [0,0]
a[(n+1)//div_n].append(n+1)
a[(n+1)//div_n].append(n+1)
a_count = [0] * (div_n)
a_count[0] += 2
a_count[(n+1)//div_n] += 2

import bisect
ans = 0
for tmp in p_ind:
    val, i = tmp
    group = i//div_n
    j = bisect.bisect(a[group],i)
    #left
    if(j>1):
        left1 = a[group][j-1]
        left2 = a[group][j-2]
    elif(j==1):
        left1 = a[group][j-1]
        lg = group-1
        while(True):
            if(a_count[lg]>0):
                break
            lg -=1
        left2 = a[lg][-1]
    else:
        lg = group-1
        while(True):
            if(a_count[lg]>0):
                break
            lg -=1
        if(a_count[lg]>=2):
            left1 = a[lg][-1]
            left2 = a[lg][-2]
        else:
            left1 = a[lg][-1]
            while(True):
                lg -=1
                if(a_count[lg]>0):
                    break
            left2 = a[lg][-1]
    #right
    if(a_count[group]>=j+2):
        right1 = a[group][j]
        right2 = a[group][j+1]
    elif(a_count[group]>=j+1):
        right1 = a[group][j]
        rg = group
        while(True):
            rg += 1
            if(a_count[rg]>0):
                break
        right2 = a[rg][0]
    else:
        rg = group
        while(True):
            rg += 1
            if(a_count[rg]>0):
                break
        if(a_count[rg]>=2):
            right1 = a[rg][0]
            right2 = a[rg][1]
        else:
            right1 = a[rg][0]
            while(True):
                rg += 1
                if(a_count[rg]>0):
                    break
            right2 = a[rg][0]

    ans += ((right2 - right1)* (i - left1) + (right1 - i)* (left1 - left2)) * val
    a[group].insert(j,i)
    a_count[group] += 1

print(ans)
