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

def z_algorithm(s):
    n = len(s)
    if(n == 0):
        return []
    if(type(s) is str):
        s2 = [0] * n
        for i, si in enumerate(s):
            s2[i] = ord(si)
        s = s2
    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if (j + z[j] <= i) else min(j + z[j] - i, z[i - j])
        while(i + z[i] < n):
            if(s[z[i]] != s[i + z[i]]):
                break
            z[i] += 1
        if(j + z[j] < i + z[i]):
            j = i
    z[0] = n
    return z

w = input()
n = len(w)

if w.count(w[0]) == n:
    print(n)
    print(1)
    exit()

front = z_algorithm(w)
back = z_algorithm(w[::-1])

def check(z):
    res = [0] * (n+1)
    for i in range(1,n//2 + 1):
        if res[i] ==1:
            continue
        for j in range(i,n-i+1,i):
            if z[j] >= i:
                res[i+j] = 1
            else:
                break
    return res


left = check(front)
right = check(back)

if left[-1] == 0:
    print(1)
    print(1)
    exit()

ans = 0
for i in range(1,n):
    if left[i] == 0 and right[n-i]==0:
        ans += 1

print(2)
print(ans)

# print(front)
# print(back)
# print(left)
# print(right)