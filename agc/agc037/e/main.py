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
s = input()
r = s[::-1]
s += '?'

ans = 'z' * n
if k == 1:
    for i in range(n+1):
        res = s[i:n] + r[:i]
        if ans > res:
            ans = res[::]
    print(ans)
    exit()

for si in 'abcdefghijklmnopqrstuvwxyz':
    if si in s:
        head = si
        break

i = 0
l = 0
def make(x,k):
    res = s[n-x:n] + r[:n-x]
    k -= 1
    return make_tail(res,k)

def make_tail(res,k):
    tail = 0
    while tail < n:
        if res[n-1-tail] != head:
            break
        tail += 1
    for i in range(k):
        res += head * tail
        tail *= 2
        if tail >= n:
            return head * n
    res = res[-n:]
    return res[::-1]



for i in range(n):
    if s[i] == head and s[i-1] != head:
        res = make(i,k)
        if ans > res:
            ans,res = res,ans

if s[-2] == head:
    res = make_tail(s[:n],k)
    if ans > res:
            ans,res = res,ans

print(ans)
    