import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# 二分木
import bisect

n,k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

len_m = bisect.bisect_left(a, 0)
len_0 = bisect.bisect_right(a, 0) - len_m
len_p = n - len_m - len_0

a_m = a[:len_m][::-1]
for i in range(len_m):
    a_m[i] = -1 * a_m[i]
a_p = a[(len_m + len_0):]

num_m = len_m * len_p
num_0 = len_0 * (n - len_0) + len_0*(len_0 - 1)//2

def calc(a1, a2, x):
    #a1[i]*a2[j]でX以上になるものの数を数える
    #a1,a2ともに正の値のみ、かつソートされているとする。
    ans = 0
    len_a2 = len(a2)
    tmp_j = len_a2
    for i in range(len(a1)):
        tmp = x/a1[i]
        tmp_j =  bisect.bisect_left(a2[:tmp_j] , tmp)
        ans += len_a2 - tmp_j
    return(ans)

def calc2(a1,a2, x):
    #a1[i]**2,a2[j]**2でX以上になるものの数を数える
    #a1,a2ともに正の値のみ、かつソートされているとする。
    ans = 0
    for ax in [a1,a2]:
        len_ax = len(ax)
        tmp_j = len_ax
        for i in range(len_ax):
            tmp = x/ax[i]
            tmp_j =  bisect.bisect_left(ax[(i+1):tmp_j] , tmp) + (i+1)
            ans += len_ax - max(tmp_j, i+1)
    return(ans)

def calc3(a1,x):
    ans = 0
    for ax in [a1]:
        len_ax = len(ax)
        tmp_j = len_ax
        for i in range(len_ax):
            tmp = x/ax[i]
            tmp_j =  bisect.bisect_left(ax[(i+1):tmp_j] , tmp) + (i+1)
            ans += len_ax - max(tmp_j, i+1)
    return(ans)


if( k <= num_m ):
    # minus
    min_ = a_m[0] * a_p[0]
    max_ = a_m[-1] * a_p[-1]
    ans = (min_ + max_)//2
    dic = {}
    count = 0
    while(count < 100000):
        # print(ans)
        # print("{} {}".format(max_, min_))
        x = calc(a_m, a_p, ans)
        x_b = calc(a_m, a_p, ans + 1)
        # print("{} {}".format(x, x_b))
        if(( x_b < k ) & ( k <= x )):
            print(ans)
            break
        elif(x_b >= k):
            min_ = max(ans, min_+1)
        else:
            max_ = ans
        ans = (min_ + max_)//2
        count += 1

elif(k <= num_m + num_0 ):
    # 0
    print(0)

else:
    # plus
    k = n*(n-1)//2 - k
    if( (len_m == 1) | (len_p == 1)):
        if(len_m == 1):
            a1 = a_p
        else:
            a1 = a_m
        min_ = a1[0] * a1[1]
        max_ = a1[-1] * a1[-2]
        ans = (min_ + max_)//2
        while(True):
            x = calc3(a1, ans)
            x_b = calc3(a1, ans+1)
            if(( x_b <= k ) & ( k < x )):
                print(ans)
                break
            elif(x_b > k):
                min_ = max(ans, min_+1)
            else:
                max_ = ans
            ans = (min_ + max_)//2
    else:
        min_ = min(a_m[0] * a_m[1], a_p[0] * a_p[1])
        max_ = max(a_m[-1] * a_m[-2], a_p[-1] * a_p[-2])
        ans = (min_ + max_)//2
        count = 0
        while(count < 100000):
            # print(ans)
            # print("{} {}".format(max_, min_))
            x = calc2(a_m, a_p, ans)
            x_b = calc2(a_m, a_p, ans+1)
            # print("{} {}".format(x, x_b))
            if(( x_b <= k ) & ( k < x )):
                print(ans)
                break
            elif(x_b > k):
                min_ = max(ans, min_+1)
            else:
                max_ = ans
            ans = (min_ + max_)//2
            count += 1
