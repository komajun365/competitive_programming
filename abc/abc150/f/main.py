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
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a += a[0:1]
b += b[0:1]

ad = [0] * n
bd = [0] * n
for i in range(n):
    ad[i] = a[i] ^ a[i+1]
    bd[i] = b[i] ^ b[i+1]

s = bd + [2**31] + ad + ad

z = z_algorithm(s)
ans = []
for i in range(n):
    j = i+n+1
    if z[j] == n:
        ans.append('{} {}'.format(i, a[i] ^ b[0]))

print('\n'.join(ans))
