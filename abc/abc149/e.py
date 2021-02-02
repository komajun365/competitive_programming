# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()

a_sum = [0] * (n+1)
for i in range(n):
    a_sum[i+1] = a_sum[i] + a[i]

min_ = 0
max_ = 2*10**5+1

for _ in range(50):
    tmp = (min_+max_)//2
    i,j = 0,n-1
    m_tmp = 0
    while(True):
        if(a[i] + a[j] >= tmp):
            m_tmp += n-i
            j -= 1
        else:
            i += 1

        if(i >= n)|(j < 0):
            break
    if(m_tmp >= m):
        min_ = tmp
    else:
        max_ = tmp

    if(max_-min_ == 1):
        break

tmp = min_
i,j = 0,n-1
m_tmp = 0
ans = 0
while(True):
    if(a[i] + a[j] >= tmp):
        m_tmp += n-i
        ans += a[j] * (n-i) + a_sum[-1] - a_sum[i]
        j -= 1
    else:
        i += 1

    if(i >= n)|(j < 0):
        break

ans -= min_ * (m_tmp - m)
print(ans)
# print(min_)
# print(max_)
# print(m_tmp)
# print(a)
# print(a_sum)
