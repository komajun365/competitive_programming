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


import sys
read = sys.stdin.buffer.read

n,m,*a = map(int,read().split())
mod = 998244353

nums = []
for i in range(n):
    num = 0
    for j in range(m):
        num = num*2 + a[i*m+j]
    nums.append(num)


def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

basis = []
for num in nums:
    x = get_base(num,basis)
    if x != 0:
        basis.append(x)

reject = n - len(basis)
ans = (pow(2,n,mod) - pow(2,reject,mod)) * pow(2,m-1,mod)
ans %= mod
print(ans)

# for _ in range(t):
#     n = int(readline())
#     a = list(map(int,readline().split()))
#     s = readline().strip()

#     basis = []
#     for si,ai in zip(s[::-1], a[::-1]):
#         x = get_base(ai,basis)
#         if(si=='0')&(x>0):
#             basis.append(x)
#         elif(si=='1')&(x>0):
#             print(1)
#             break
#     else:
#         print(0)