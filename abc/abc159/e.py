# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

h,w,k = map(int,input().split())
s = [tuple(map(int, input())) for _ in range(h)]

sum_w = [[0] * (w+1) for _ in range(h)]
for i in range(h):
    for j in range(1,w+1):
        sum_w[i][j] = sum_w[i][j-1] + s[i][j-1]

# sum_h = [[0] * w for _ in range(h+1)]
# for i in range(1,h+1):
#     for j in range(w):
#         sum_h[i][j] = sum_h[i-1][j] + sum_w[i-1][j+1]

sums = []
for i in range(h):
    sums.append([[0] * w for _ in range(h+1)])

for i in range(h):
    for j in range(i+1,h+1):
        for l in range(w):
            sums[i][j][l] = sums[i][j-1][l] + sum_w[j-1][l+1]

ans = h + w
for i in range(2**(h-1)):
    nums = []
    for j in range(h-1):
        if((i >> j)&1 == 1):
            nums.append(j+1)
    tmp = len(nums)
    print('{} {}'.format(i,tmp))
    nums.append(h)
    # print(nums)
    head = 0
    checks = []
    for j in nums:
        checks.append(sums[head][j])
        head = j
    # print(i)
    print(checks)

    minus_num = [0] * len(checks)
    w_now = 0
    NG_flag = 0
    cut_flag = 0
    for j in range(w):
        print(minus_num)
        if(NG_flag == 1):
            break
        for l in range(len(checks)):
            check_num = checks[l][j] - minus_num[l]
            print(check_num)
            if(check_num > k):
                if(w_now == 0):
                    print('hoge')
                    NG_flag = 1
                    break
                cut_flag = 1
                break


        if(cut_flag==1):
            # print('j={}'.format(j))
            tmp += 1
            for l in range(len(checks)):
                minus_num[l] = checks[l][j-1]
                check_num = checks[l][j] - minus_num[l]
                print('hoge {}'.format(check_num))
                if(check_num > k):
                    NG_flag=1
                    break
            cut_flag = 0
            w_now = 1
        else:
            w_now += 1

    # print('')
    # print(tmp)
    if(NG_flag==0):
        ans = min(ans, tmp)
        # print('ans = {}'.format(ans))


print(ans)
print(sums)
