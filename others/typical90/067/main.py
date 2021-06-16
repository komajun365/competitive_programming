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

num = 0
for ni in str(n):
    num = num*8 + int(ni)

def excute(x):
    res = 0
    cnt = 0
    while x > 0:
        tmp = x % 9
        if tmp == 8:
            tmp = 5
        res += tmp * 8**cnt
        x //= 9
        cnt += 1
    return res

for _ in range(k):
    num = excute(num)

ans = 0
cnt = 0
while num > 0:
    tmp = num % 8
    ans += tmp * 10**cnt
    num //= 8
    cnt += 1
print(ans)

