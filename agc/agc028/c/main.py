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

n,*ab = map(int,read().split())
nums = sorted(ab)
n_num = nums[n-1]
l_ind = 0
r_ind = 0
left,right = [],[]
it = iter(ab)
for a,b in zip(it,it):
    if (a <= n_num and b <= n_num) or (a > n_num and b > n_num):
        print(sum(nums[:n]))
        exit()
    
    if(a < b):
        left.append([a,b,l_ind])
        l_ind += 1
    else:
        right.append([a,b, r_ind])
        r_ind += 1

if l_ind == n or l_ind == 0:
    print(sum(nums[:n]))
    exit()

fix_num = 0
if l_ind == 1:
    left.append( [left[0][0],left[0][1],1] )
    fix_num -= left[0][0]
if r_ind == 1:
    right.append( [right[0][0],right[0][1],1] )
    fix_num -= right[0][0]

la_sort = sorted(left, key=lambda x: x[0])
lb_sort = sorted(left, key=lambda x: x[1])
ra_sort = sorted(right, key=lambda x: x[0])
rb_sort = sorted(right, key=lambda x: x[1])

ans = sum(nums)
tot_n = sum(nums[:n])
for i in range(l_ind):
    a_small = left[i][0]
    b_large = lb_sort[0][1]
    if(left[i][2] == lb_sort[0][2]):
        b_large = lb_sort[1][1]
    for j in range(2):
        a_large = ra_sort[j][0]
        b_small = rb_sort[0][1]
        if( ra_sort[j][2] == rb_sort[0][2] ):
            b_small = rb_sort[1][1]
        tmp = tot_n - max(a_small, b_small) + min(a_large, b_large)
        ans = min(ans,tmp)

for j in range(r_ind):
    b_small = right[j][1]
    a_large = ra_sort[0][0]
    if( right[j][2] == ra_sort[0][2] ):
        a_large = ra_sort[1][0]
    for i in range(2):
        b_large = lb_sort[0][1]
        a_small = la_sort[0][0]
        if lb_sort[0][2] == la_sort[0][2]:
            a_small = la_sort[1][0]
        tmp = tot_n - max(a_small, b_small) + min(a_large, b_large)
        ans = min(ans,tmp)

print(ans)


    
