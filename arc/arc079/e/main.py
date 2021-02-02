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
a = list(map(int,input().split()))

ans = 0
tot = sum(a)
if(tot > n**2):
    cnt = tot - n**2
    cnt2 = 0
    for i,ai in enumerate(a):
        ai += cnt
        cnt2 += ai//(n+1)
        ai %= (n+1)
        a[i] = ai
    
    a.sort()
    rem = cnt2 - cnt
    for i in range(n):
        if(i < rem):
            a[i] += n+1
    ans = cnt

def calc(a):
    max_num = -1
    max_ind = -1
    min_num = 10**17
    for i,ai in enumerate(a):
        if(max_num < ai):
            max_ind = i
            max_num = ai
        a[i] += 1
    if(max_num <= n-1):
        print(ans)
        exit()
    a[max_ind] -= n+1
    return a

while(max(a) >= n):
    a = calc(a)
    ans += 1

print(ans)

