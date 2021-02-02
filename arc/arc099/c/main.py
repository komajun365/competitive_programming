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

n,k = map(int,input().split())
a = list(map(int,input().split()))
print(-((-n+1)//(k-1)))

# a_ind = 0
# for i,ai in enumerate(a):
#     if ai==1:
#         a_ind = i
#         break
# l = a_ind
# r = n - a_ind - 1
# ans = 0
# for x in [l,r]:
#     ans -= -x//(k-1)
# print(ans)