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

n,b = map(int,input().split())
l = len(str(n))

ans = 0
def check(fx):
    x = b + fx
    if x > n:
        return 0
    y = x
    z = 1
    while y > 0:
        z *= y%10
        y //= 10
    if fx == z:
        return 1
    else:
        return 0

for fx in [0,1]:
    ans += check(fx)

nums = [1]
for p,a in zip([2,3,5,7],[3,2,1,1]):
    head = len(nums)
    for mul in range(1, a*l+1):
        base = p**mul
        for i in nums[:head]:
            i *= base
            if i <= n-b:
                nums.append(i)
                ans += check(i)

print(ans)

            

