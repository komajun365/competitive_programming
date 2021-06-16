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
    if n == 0:
        return []
    if type(s) is str:
        s2 = [0] * n
        for i, si in enumerate(s):
            s2[i] = ord(si)
        s = s2
    z = [0] * n
    j = 0
    for i in range(1, n):
        z[i] = 0 if (j + z[j] <= i) else min(j + z[j] - i, z[i - j])
        while i + z[i] < n:
            if s[z[i]] != s[i + z[i]]:
                break
            z[i] += 1
        if j + z[j] < i + z[i]:
            j = i
    z[0] = n
    return z

n = int(input())
d = {'R':0, 'G':1, 'B':2}
s = [d[x] for x in input()]
t = [d[x] for x in input()]

def calc(x,y):
    xl = len(x)
    yl = len(y)
    z = x[::-1] + [9]
    for i in range(3):
        for j in range(yl-1,-1,-1):
            z.append((i-y[j])%3)
        z.append(9)
    
    cnt = z_algorithm(z)
    res = 0
    for i in range(3):
        for j in range(yl):
            idx = xl + 1 + i * (yl+1) + j
            if cnt[idx] >= yl - j:
                res += 1
    return res

ans = calc(s,t) + calc(t,s[:n-1])
print(ans)