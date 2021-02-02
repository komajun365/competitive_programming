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

n,t = map(int,input().split())
a = list(map(int,input().split()))

if(n==1):
    if(a[0] > t):
        print(0)
    else:
        print(a[0])
    exit()

n2 = n//2
a1 = a[:n2]
a2 = a[n2:]

def calc(x):
    res = [0]
    m = len(x)
    for i in range(m):
        mm = len(res)
        for j in range(mm):
            res.append(res[j] + x[i])
    return res

x1 = calc(a1)
x2 = calc(a2)
x1.sort()
x2.sort(reverse=True)

ans = 0
j = 0
for i in range(len(x1)):
    while(j < len(x2)):
        if(x1[i] + x2[j]) <= t:
            ans = max(ans,x1[i] + x2[j])
            break
        else:
            j += 1

print(ans)
# print(x1)
# print(x2)
