# oj t -c "python main.py" -d "./tests/" 

# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

# import sys
# import os
# f = open('../../../input.txt', 'r')
# sys.stdin = f

import sys
read = sys.stdin.buffer.read

l,n,*x = map(int,read().split())

left = [0] * (n+1)
for i in range(n):
    left[i] = left[i-1] + x[i]*2

right = [0] * (n+1)
for i in range(n-1,-1,-1):
    right[i] = right[i+1] + (l-x[i])*2

ans = max(l - x[0], x[-1])
#最後に i -> i+1
for i in range(n-1):
    l_num = i+1
    r_num = n-i-2
    tmp = -x[i] + max(x[i+1]-x[i], l - (x[i+1]-x[i]))
    if l_num > r_num:
        tmp += right[i+2]
        tmp += left[i] - left[l_num-r_num-2]
    elif l_num == r_num:
        tmp += right[i+2]
        tmp += left[i]
    else:
        tmp += right[i+2] - right[ n-(r_num-l_num) ]
        tmp += left[i]
    ans = max(ans,tmp)
    # print(i,l_num,r_num,tmp)

#最後に i+1 -> i
for i in range(n-1):
    l_num = i
    r_num = n-i-1
    tmp = -(l-x[i+1]) + max(x[i+1]-x[i], l - (x[i+1]-x[i]))
    if r_num > l_num:
        tmp += left[i-1]
        tmp += right[i+1] - right[n-1-(r_num-l_num-2)]
    elif l_num == r_num:
        tmp += left[i-1]
        tmp += right[i+1]
    else:
        tmp += left[i-1] - left[l_num-r_num-1]
        tmp += right[i+1]
    ans = max(ans,tmp)
    # print(i,l_num,r_num,tmp)

print(ans)
print(left)
print(right)