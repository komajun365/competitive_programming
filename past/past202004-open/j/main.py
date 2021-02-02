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

s = input()

def calc(x):
    n = len(x)
    l = -1
    r = -1
    for i in range(n):
        if(x[i] == '('):
            l = i
        if(x[i] == ')'):
            r = i
            break
    if(l == -1):
        print(x)
        exit()
    mid = x[l+1:r]
    res = x[:l] + mid + mid[::-1] + x[r+1:]
    # print(l,r)
    # print(res)
    return res

for _ in range(1000):
    s = calc(s) 
