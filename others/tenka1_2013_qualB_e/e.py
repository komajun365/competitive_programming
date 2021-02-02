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

def solve_t(n,xy):
    res = 0
    x = xy[0][0]
    y = xy[0][1]
    done = [0] * n
    done[0] = 1
    for _ in range(n-1):
        cand = []
        for i in range(n):
            if(done[i]==1):
                continue
            tmp = (xy[i][0]-x)**2 + (xy[i][1]-y)**2
            cand.append((tmp,i))
        cand.sort()
        res += cand[0][0]**0.5
        next = cand[0][1]
        x,y = xy[next]
        done[next] = 1
    return res

def solve_c(n,xy):
    res = 0
    x = xy[0][0]
    y = xy[0][1]
    done = [0] * n
    done[0] = 1
    for _ in range(n-1):
        cand = []
        for i in range(n):
            if(done[i]==1):
                continue
            tmp = (xy[i][0]-x)**2 + (xy[i][1]-y)**2
            cand.append((tmp,i))
        cand.sort()
        ind = 1
        if(len(cand)<=2):
            ind = 0
        res += cand[ind][0]**0.5
        next = cand[ind][1]
        x,y = xy[next]
        done[next] = 1
    return res

# xy_samp= [[4,6],[2,5],[6,10],[1,2],[1,6]]
xy_samp = []

for i in range(50):
    xy_samp.append([i*8,7])
    xy_samp.append([i*8+4,0])

n = len(xy_samp)

print(n)
for i in xy_samp:
    print(' '.join(map(str,i)))


print(solve_t(n,xy_samp))
print(solve_c(n,xy_samp))


'''




'''
