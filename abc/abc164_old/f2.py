# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
s = list(map(int,input().split()))
t = list(map(int,input().split()))
u = list(map(int,input().split()))
v = list(map(int,input().split()))

a = [[0] * n for _ in range(n)]

if(n==1):
    if(u[0]==v[0]):
        print(u[0])
    else:
        print(-1)
    exit()


for i in range(64):
    col = [0]*n
    row = [0]*n
    remain_col = []
    remain_row = []
    use_col = set()
    use_row = set()
    for j in range(n):
        num = (u[j] >> i)&1
        if(s[j]==0)&(num==1):
            col[j]=1
            use_col.add(1)
        elif(s[j]==1)&(num==0):
            col[j]=0
            use_col.add(0)
        elif(s[j]==0)&(num==0):
            col[j]= -10
            remain_col.append(j)
        else:
            col[j]= -11
            remain_col.append(j)

    for j in range(n):
        num = (v[j] >> i)&1
        if(t[j]==0)&(num==1):
            row[j]=1
            use_row.add(1)
        elif(t[j]==1)&(num==0):
            row[j]=0
            use_row.add(0)
        elif(t[j]==0)&(num==0):
            row[j]= -10
            remain_row.append(j)
        else:
            row[j]= -11
            remain_row.append(j)

    if(len(use_row)+len(use_row)>=3):
        print(-1)
        exit()

    rem_len_col = len(remain_col)
    rem_len_row = len(remain_row)
    remains = [[-1] * rem_len_row for _ in range(rem_len_col) ]

    if(len(use_col)==1)&(len(use_row)==1):
        if(list(use_col)[0] != list(use_row)[0]):
            print(-1)
            exit()
        used = list(use_col)[0]
        for j in range(rem_len_col):
            for k in range(rem_len_row):
                remains[j][k] = 1-used
    elif(len(use_col)==1)&(len(use_row)==0):
        used = list(use_col)[0]
        for j in range(rem_len_col):
            for k in range(rem_len_row):
                remains[j][k] = 1-used
    elif(len(use_col)==0)&(len(use_row)==1):
        used = list(use_row)[0]
        for j in range(rem_len_col):
            for k in range(rem_len_row):
                remains[j][k] = 1-used
    else:
        for j in range(rem_len_col):
            for k in range(rem_len_row):
                remains[j][k] = (j+k)%2

    rem_c = 0
    for j in range(n):
        rem_r = 0
        for k in range(n):
            if(col[j] >= 0):
                a[j][k] += col[j] << i
            elif(row[k] >= 0):
                a[j][k] += row[k] << i
            else:
                # print(remains)
                # print(col)
                # print(row)
                # print((i,j,k,rem_c,rem_r))
                a[j][k] += (remains[rem_c][rem_r]) << i
                rem_r += 1
        if(col[j] < 0):
            rem_c += 1

for i in a:
    print(' '.join(map(str, i)))
