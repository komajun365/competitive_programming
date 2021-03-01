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

k = int(input())
s = input()
t = input()

rem = [k] * 10
rem[0] = 0
tak = [0] * 10
ao = [0] * 10


for i in range(4):
    num = int(s[i])
    tak[num] += 1
    rem[num] -= 1
    num = int(t[i])
    ao[num] += 1
    rem[num] -= 1

def score(x):
    res = 0
    for i in range(1,10):
        res += i * 10 ** x[i]
    return res

tot = 0
win = 0

for i in range(10):
    for j in range(10):
        if i == j:
            if rem[i] < 2:
                continue
            tak[i] += 1
            ao[j] += 1
            cnt = rem[i] * (rem[i]-1)
            tot += cnt
            if score(tak) > score(ao):
                win += cnt
            tak[i] -= 1
            ao[j] -= 1
        else:
            if rem[i] == 0 or rem[j] == 0:
                continue
            tak[i] += 1
            ao[j] += 1
            cnt = rem[i] * rem[j]
            tot += cnt
            if score(tak) > score(ao):
                win += cnt
            tak[i] -= 1
            ao[j] -= 1

print(win/tot)
