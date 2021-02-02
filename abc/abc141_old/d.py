import math

n,m = map(int, input().split())
a_list = list(map(int, input().split()))

a_list.sort()

a_logs = list(map(lambda x: int(math.log2(x)), a_list))
max_num = max(a_logs)
num = max_num*1

count_num = 0
flag = True
while(flag):
    count_num_temp = a_logs.count(num) + count_num*2
    if(count_num_temp > m):
        flag = False
        remain = m - count_num
    else:
        count_num = count_num_temp
        num -= 1
        if(num == -1):
            print('0')
            exit()

for i,a_log in enumerate(a_logs):
    if(a_log > num):
        a_list[i] = a_list[i] // (2**(a_log-num))

if(remain > 0):
    a_list.sort
    for i in range(remain):
        i = (n-1) -i
        a_list[i] = a_list[i] //2

ans = sum(a_list)
print(ans)
