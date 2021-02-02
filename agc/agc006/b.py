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

n,x = map(int,input().split())

if(x==1)|(x==2*n-1):
    print('No')
    exit()

if(n==2):
    print('Yes')
    print('\n'.join(map(str,[1,2,3])))
    exit()

m = 2*n-1
ans = list(range(1,m+1))
ans = ans + ans
center = m//2
if(x-1 < center):
    ans = ans[m+x-1-center : m+m+x-1-center]
else:
    ans = ans[x-1-center : m+x-1-center]

if not ((x==2)|(x==m-1)):
    ans[center-2],ans[center+2] = ans[center+2],ans[center-2]

print('Yes')
print('\n'.join(map(str,ans)))



# import itertools
#
# p = itertools.permutations(range(1,6), 5)
# for i in p:
#     i = list(i)
#     ans1 = []
#     for j in range(3):
#         tmp = i[j:j+3]
#         tmp.sort()
#         ans1.append(tmp[1])
#     ans1.sort()
#     ans1 = ans1[1]
#
#     ans2 = i + i[1:4] + i[2::3]
#     ans2.sort()
#     ans2 = ans2[4]
#
#     if(ans1!=ans2):
#         print('NG')
#         print(i)
#         exit()
#
# print('done')
#
# '''
#
#
# 1
# 1,1,1
# 1,2,3,2,1
# 1,3,6,7,6,3,1
# 1,4,10,16,19,16,10,4,1
#
#
#
# '''
