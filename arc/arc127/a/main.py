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

n = input()

def calc(x):
    #xケタ
    res = 0
    for i in range(x):
        res += 10**i
    return res

# def calc2(x,y):
#     #xケタで先頭y個まで1でそのあと0
#     res = 0
#     for i in range(y):
#         res += 10**(x-i-1)
#     return res

l = len(n)
ans = 0
for i in range(1,l):
    ans += calc(i)

for i in range(l):
    if int(n[i]) >= 2:
        ans += calc(l-i)
        break
    if int(n[i]) == 0:
        break
    if i != l-1:
        ans += int(n[i+1:]) + 1
    else:
        ans += 1

print(ans)

# for i in range(1,10):
#     print(calc(i), calc2(i,i-1))
