# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

import sys
read = sys.stdin.read
import math

t,p,*data = read().split()
t = int(t)

def solve(s):
    score = []
    for si in s:
        score.append([int(i) for i in si])
    skill = [0] * 100
    diff = [0] * 10000
    for i in range(100):
        for j in range(10000):
            skill[i] += score[i][j]
            diff[j] += score[i][j]

    for i in range(100):
        if skill[i] == 10000:
            skill[i] = 3.0
        else:
            skill[i] = max(-3.0, min(3.0, math.log(skill[i] / (10000- skill[i]))))

    for i in range(10000):
        if diff[i] == 0:
            diff[i] = -3.0
        else:
            diff[i] = max(-3.0, min(3.0, math.log((100- diff[i])/ diff[i])))
    
    ab_score = [0] * 100
    for i in range(100):
        if skill[i] < -0.5:
            ab_score[i] = 0
            continue
        cnt = 0
        for j in range(10000):
            if score[i][j] == 0:
                p = 1 / (1 + math.exp(skill[i] - diff[j]))    
                ab_score[i] -= math.log(1-p)
                cnt += 1
        ab_score[i] /= max(1,cnt)
    
    res = 1
    max_score = ab_score[0]
    for i in range(1,100):
        if ab_score[i] > max_score:
            res = i+1
            max_score = ab_score[i]
        print(i+1, ab_score[i])#, skill[i])

    return res

ans = [''] * t
idx = 0
for i in range(t):
    s = data[idx:idx+100]
    idx += 100
    res = solve(s)
    ans[i] = 'Case #{}: {}'.format(i+1,res)
print('\n'.join(ans))


