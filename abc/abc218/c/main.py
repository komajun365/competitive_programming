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
s = []
for _ in range(n):
    s.append([])
    x = input()
    for xi in x:
        s[-1].append((xi == '#') * 1)
    for _ in range(n):
        s[-1].append(0)
for _ in range(n):
    s.append([0] * (n*2))
t = []
for _ in range(n):
    t.append([])
    x = input()
    for xi in x:
        t[-1].append((xi == '#') * 1)

tot_s = 0
for si in s:
    tot_s += sum(si)
tot_t = 0
for ti in t:
    tot_t += sum(ti)
if tot_s != tot_t:
    print('No')
    exit()


def rotate(x):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[n-j-1][i] = x[i][j]
    return res

def get_base(x):
    for i in range(n):
        for j in range(n):
            if x[i][j] == 1:
                return [i,j] 
    
si,sj = get_base(s)

for _ in range(4):
    ti,tj = get_base(t)
    check = True
    for i in range(n):
        for j in range(n):
            if s[si-ti+i][sj-tj+j] != t[i][j]:
                check = False
    if check:
        print('Yes')
        exit()
    
    t = rotate(t)

print('No')

