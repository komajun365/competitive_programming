import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

import bisect
n_m = bisect.bisect_left(a, 0)
n_0 = bisect.bisect_left(a, 1) - n_m
n_p = n - (n_m + n_0)

nn_p = n - (n_m * n_p + n_0 * (n - n_0) + n_0*(n_0-1)//2)

if( n_m * n_p < k)&(k <= n - nn_p):
    print(0)
    exit()

def calc_m(a, b, len_a, len_b, x):
    i = len_a-1
    j = 0
    cnt = 0
    while(True):
        tmp = a[i] * b[j]
        if( tmp < x):
            cnt += i+1
            j += 1
        else:
            i -= 1

        if(i < 0)|(j >= len_b):
            break
    return cnt

def calc_p(a,len_a, x):
    if(len_a <= 1):
        return 0

    i = len_a - 1
    j = 0
    cnt = 0
    while(True):
        tmp = a[i] * a[j]
        if( tmp < x):
            cnt += i+1 - ( i >= j)
            j += 1
        else:
            i -= 1

        if(i < 0)|(j >= len_a):
            break
    return cnt//2

if( n_m * n_p >= k):
    a_m = tuple(a[:n_m])
    a_p = tuple(a[  :(n - n_p -1):-1])

    ul = [a_m[-1] * a_p[-1]+1, n_m*n_p]
    dl = [a_m[0] * a_p[0]-1, 0]

    while(True):
        if(ul[0] - dl[0] == 1):
            break
        mid = (dl[0] + ul[0])//2
        mid_cnt = calc_m(a_m,a_p,n_m,n_p, mid)

        if( mid_cnt < k):
            dl = [ mid, mid_cnt ]
        else:
            ul = [ mid, mid_cnt ]

    print(dl[0])

else:
    k = k - (n - nn_p)
    a_m = tuple(a[n_m - 1::-1])
    a_p = tuple(a[ (n - n_p) :])

    if(n_m <= 1):
        ul = [a_p[-1] * a_p[-2]+1, nn_p]
        dl = [a_p[0] * a_p[1]-1, 0]
    elif(n_p <= 1):
        ul = [a_m[-1] * a_m[-2]+1, nn_p]
        dl = [a_m[0] * a_m[1]-1, 0]
    else:
        ul = [max(a_m[-1] * a_m[-2]+1 ,a_p[-1] * a_p[-2]+1), nn_p]
        dl = [min(a_p[0] * a_p[1]-1 ,a_m[0] * a_m[1]-1), 0]

    while(True):
        if(ul[0] - dl[0] == 1):
            break
        mid = (dl[0] + ul[0])//2
        mid_cnt = calc_p(a_m,n_m, mid) + calc_p(a_p,n_p, mid)

        if( mid_cnt < k):
            dl = [ mid, mid_cnt ]
        else:
            ul = [ mid, mid_cnt ]

    print(dl[0])

# print(k)
# print(ul)
# print(dl)
# print('{} {} {}'.format(n_m,n_0,n_p))
# print(a_m)
# print(a_p)
