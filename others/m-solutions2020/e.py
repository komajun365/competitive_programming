# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import itertools
import bisect

n = int(input())
xyp = tuple([tuple(map(int,input().split())) for _ in range(n)])

ans = []

def calc(x,y,i):
    tmp = 10**10
    xi,yi = xyp[i][:2]
    x_ind = bisect.bisect_left(x,xi)
    y_ind = bisect.bisect_left(y,yi)
    if(x_ind==0):
        tmp = min(tmp, x[0]-xi)
    elif(x_ind==len(x)):
        tmp = min(tmp, xi - x[x_ind-1])
    else:
        tmp = min(tmp, x[x_ind]-xi)
        tmp = min(tmp, xi - x[x_ind-1])

    if(y_ind==0):
        tmp = min(tmp, y[0]-yi)
    elif(y_ind==len(y)):
        tmp = min(tmp, yi - y[y_ind-1])
    else:
        tmp = min(tmp, y[y_ind]-yi)
        tmp = min(tmp, yi - y[y_ind-1])
    # print(x)
    # print(y)
    # print(i,xi,yi,tmp*xyp[i][2])
    # print('')

    return tmp* xyp[i][2]

tmp = 0
for i in range(n):
    tmp += calc([0],[0],i)
ans.append(tmp)

for i in range(1,n+1):
    tmp = 10**10
    for c in itertools.combinations(range(n), i):
        d = []
        for j in range(n):
            if(not j in c):
                d.append(j)
        for j in range(2**i):
            x = [0]
            y = [0]
            tmp2 = 0
            for k in range(i):
                if(j>>k)&1:
                    y.append(xyp[c[k]][1])
                else:
                    x.append(xyp[c[k]][0])
            x.sort()
            y.sort()
            for k in d:
                tmp2 += calc(x,y,k)
            tmp = min(tmp,tmp2)
    ans.append(tmp)

print('\n'.join(map(str,ans)))





# tot = 0
# for i in range(1,16):
#     tmp = 1
#     for j in range(15,15-i,-1):
#         tmp *= j
#     for j in range(1,i+1):
#         tmp //=j
#     tmp *= 2**j
#     print(i,tmp)
#     tot += tmp
#
# print('tot',tot)

'''
どれかに通すべきなので候補は30本
30C15


'''
