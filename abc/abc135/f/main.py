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

s = input()
t = input()
ls = len(s)
lt = len(t)

num = -((-lt) // ls)
s2 = t + s * (num+1)

z = z_algorithm(s2)

deg_in = [0] * ls
deg_out = [0] * ls
for i in range(ls):
    if z[i+lt] >= lt:
        deg_out[i] += 1
        deg_in[(i+lt)%ls] += 1

ans = 0
done = [0] * ls
for i in range(ls):
    if done[i] == 1:
        continue
    if deg_in[i] == 0:
        cnt = 0
        j = i
        done[i] = 1
        while deg_out[j] == 1:
            cnt += 1
            j = (j + lt)% ls
            done[j] = 1
        ans = max(ans,cnt)

if min(done) == 0:
    print(-1)
    exit()

print(ans)


