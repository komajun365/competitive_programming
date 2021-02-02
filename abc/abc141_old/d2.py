import math
import numpy as np

# n, m = 4,4
# a_list = np.array([1,9,3,5])

n,m = map(int, input().split())
a_list = np.array(list(map(int, input().split())))

# a_list = np.sort(a_list)

a_logs = np.log2(a_list).astype('int64')

max_num = max(a_logs)
num = max_num*1

count_num = 0
flag = True
while(flag):
    count_num_temp = sum(a_logs>=num) + count_num
    if(count_num_temp > m):
        flag = False
        remain = m - count_num
    else:
        count_num = count_num_temp
        num -= 1
        if(num == -1):
            print('0')
            exit()

a_list = a_list // 2**((a_logs > num) * (a_logs - num))

if(remain > 0):
    a_list = np.sort(a_list)
    a_list[(n-remain):] = a_list[(n-remain):] //2

ans = sum(a_list)
print(ans)
