import sys
import os
f = open('../input.txt', 'r')
sys.stdin = f

###################

n = int(input())
a = list(map(int, input().split()))

sum_temp = 0
count = 0
left = 0

for i in range(n):

    while( i >= left):
        check = sum_temp & a[i]
        if check > 0:
            sum_temp -= a[left]
            left += 1
        else :
            count += (i-left) + 1
            sum_temp += a[i]
            break

print(count)
