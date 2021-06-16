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

from array import array
import gc

n = int(input())
if n == 1:
    print(1)
    exit()

t = []
for _ in range(n):
    s,e = map(lambda x: x[:2]+x[3:],input().split())
    t.append([int(s),int(e)])

def check_dup2(s1,e1,s2,e2):
    if s1 <= s2 < e1 or s1 < e2 <= e1:
        return True
    return False


def check_dup(a,b):
    s1,e1 = t[a]
    s2,e2 = t[b]
    if check_dup2(s1,e1,s2,e2):
        return True
    if check_dup2(s2,e2,s1,e1):
        return True
    if e1 >= 2400:
        s1 -= 2400
        e1 -= 2400
    else:
        s1 += 2400
        e1 += 2400
    if check_dup2(s1,e1,s2,e2):
        return True
    if check_dup2(s2,e2,s1,e1):
        return True
    return False

gc.collect()

gr = [[0]*n for _ in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if not check_dup(i,j):
            gr[i][j] = 1
            gr[j][i] = 1

def check_one(x):
    flags = []
    for i in range(n):
        if (x >> i) & 1:
            for j in flags:
                if gr[i][j] == 0:
                    return False
            flags.append(i)
    return True

dp = array('B')
for i in range(1<<(n-1)):
    dp.append(n*16+n)

def read_dp(p):
    p1,p2 = divmod(p,2)
    res = dp[p1]
    if p2 == 0:
        return res % 16
    else:
        return res // 16

def min_dp(p,x):
    p1,p2 = divmod(p,2)
    now1,now2 = divmod(dp[p1],16)
    if p2 == 0:
        now = now2
    else:
        now = now1
    if now > x:
        if p2 == 0:
            now = now1 * 16 + x
        else:
            now = x * 16 + now2
        dp[p1] = now

gc.collect()     

for i in range(1,1<<n):
    if check_one(i):
        min_dp(i,1)
        continue

    x = (i-1) & i
    while x > 0:
        y = i ^ x
        tmp = read_dp(x)+read_dp(y)
        min_dp(i,tmp)
        x = (x-1) & i

print(read_dp((1<<n) - 1))
# print(dp)
# for i in gr:
#     print(i)