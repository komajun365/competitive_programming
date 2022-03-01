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
x = input()
l = len(x)
x2 = [0] * n
for i in range(l):
    x2[l-1-i] = int(x[i])

# def minus1():
#     global l
#     for i in range(n):
#         if x2[i] == 1:
#             x2[i] = 0
#             if i == l-1:
#                 l -= 1
#             break
#         x2[i] = 1

def minus(k):
    #k桁目から1を引く
    global l
    if l == k:
        x2[k-1] = 0
        for i in range(k-2,-1,-1):
            if x2[i] == 1:
                l = i+1
                return
        l = 0
        return

    for i in range(k-1,n):
        if x2[i] == 1:
            x2[i] = 0
            if i == l-1:
                l -= 1
            break
        x2[i] = 1

ans = '1'
minus(1)
for i in range(1,n):
    if l == 0:
        break
    if l < n-i+1:
        ans += '0'
        minus(1)
    else:
        ans += '1'
        minus(n-i+1)
    # print(x2[:10])

print(ans)

# n = int(input())
# x = int(input(),2)

# ans = '1'
# x -= 1
# for i in range(1,n):
#     if x == 0:
#         break
#     x -= 1
#     if x < (1<<(n-i))-1:
#         ans += '0'
#     else:
#         ans += '1'
#         x -= (1<<(n-i))-1
#     # print(i,ans,x)

# print(ans)


