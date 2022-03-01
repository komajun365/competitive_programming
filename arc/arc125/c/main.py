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

import bisect

n,k = map(int,input().split())
a = list(map(int,input().split()))
a2 = [0] + a

ans = []
for i in range(k-1):
    x = list(range(a2[i]+1, a2[i+1]+1))
    ans += x[::-1]

x = list(range(a2[k-1]+1, n+1))
ans += x[::-1]
print(' '.join(map(str,ans)))
# print(ans)



# a2 = [0] + a + [n+1]

# nums = []
# for i in range(k+1):
#     nums.append(list(range(a2[i]+1, a2[i+1])))

# ans = []
# lis = []

# def add(x):
#     if lis:
#         if lis[-1] < x:
#             lis.append(x)
#         else:
#             idx = bisect.bisect_left(lis, x)
#             lis[idx] = x
#     else:
#         lis.append(x)

# cnt = 0
# for i in range(k-1):
#     ans.append(a[i])
#     add(a[i])

#     l = len(nums[i])

#     for j in range(l):
#         x = nums[i][j]
#         if len(lis) < k-2 and len(lis) < i+1:
#             ans.append(x)
#             add(x)
#             continue
#         else:
#             for m in range(l-1, j-1, -1):
#                 x = nums[i][m]
#                 ans.append(x)
#                 add(x)
#             break

# x = nums[-2] + nums[-1] + [a[-1]]
# x.sort(reverse=True)
# ans += x

# # print(nums)
# print(' '.join(map(str,ans)))





