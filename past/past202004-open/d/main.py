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
ans = 0
def check(s,t):
    ns = len(s)
    nt = len(t)
    if(ns < nt):
        return 0
    for i in range(ns-nt+1):
        for j in range(nt):
            if(t[j] == '.'):
                continue
            if(s[i+j] == t[j]):
                continue
            break
        else:
            return 1
    return 0

ch = 'abcdefghijklmnopqrstuvwxyz.'
words1 = []
for ci in ch:
    if(check(s,ci)):
        ans += 1
        words1.append(ci)

words2 = []
for w1 in words1:
    for w2 in words1:
        w = w1+w2
        if(check(s,w)):
            ans += 1
            words2.append(w)

for w1 in words2:
    for w2 in words1:
        w = w1+w2
        if(check(s,w)):
            ans += 1

# print(words1)
# print(words2)
print(ans)