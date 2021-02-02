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

n = int(input())
s = input()

def check_cs(x):
    res = []
    now = 0
    for xi in x:
        if(xi == "E"):
            now += 1
        res.append(now)
    return res

cs_p = check_cs(s)
cs_m = check_cs(s[::-1])[::-1]
ans = n
for i in range(n):
    tmp = 0
    if(i != 0):
        tmp += i - cs_p[i-1]
    if(i != n-1):
        tmp += cs_m[i+1]
    ans = min(ans,tmp)
print(ans) 


