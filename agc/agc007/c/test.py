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

import itertools

n = 5
d1 = 2.4
x = 0

point = [0] * (n*2+1)
for i in range(n*2):
    point[i+1] = point[i] + d1 + i*x

ans = 0
prob = [[0] * (2*n+1) for _ in range(2*n+1)]
for p in itertools.permutations(range(n)):
    p = list(p)
    for bit in range(1<<n):
        tmp = 0
        done = [0] * (n+1)
        for i in range(n):
            x = p[i]
            lr = (bit >> i) & 1
            start = x * 2 + 1
            if lr == 0:
                while True:
                    if done[x] == 0:
                        done[x] = 1
                        goal = x*2
                        break
                    x -= 1
            else:
                while True:
                    if done[x+1] == 0:
                        done[x+1] = 1
                        goal = (x+1)*2
                        break
                    x += 1
            tmp += abs(point[start] - point[goal])
            prob[start][goal] += 1
        ans += tmp

fac = 1
for i in range(1,n+1):
    fac *= i
ans /= 2**n * fac
print(ans)

for i in prob:
    print(i)


"""
3 4 0
1 : 41 + 36 + 41 = 118 
2 : 4 + 6 + 6 + 4 = 20
3 : 3 + 3 = 6

4 3 0 
1 : 


"""