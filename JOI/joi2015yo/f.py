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

import bisect
class Seg_min():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**18
        self.func = min

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele_min]*2*self.num_max

        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def update(self,i,x):
        i += self.num_max
        self.x[i] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele_min
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])
                break
            if(i&1):
                res = self.func(res,self.x[i])
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])
                j -= 1
            i = i>>1
            j = j>>1
        return res
class Seg_max():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**18 * -1
        self.func = max

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [self.ide_ele_min]*2*self.num_max

        for i,num in enumerate(x, self.num_max):
            self.x[i] = num
        for i in range(self.num_max-1,0,-1):
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def update(self,i,x):
        i += self.num_max
        self.x[i] = x
        while(i>0):
            i = i//2
            self.x[i] = self.func(self.x[i<<1],self.x[(i<<1) + 1])

    def query(self,i,j):
        res = self.ide_ele_min
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                res = self.func(res,self.x[i])
                break
            if(i&1):
                res = self.func(res,self.x[i])
                i += 1
            if(not j&1):
                res = self.func(res,self.x[j])
                j -= 1
            i = i>>1
            j = j>>1
        return res

n,d = map(int,input().split())
xy = [tuple(map(int,input().split())) for _ in range(n)]

if(n==1):
    x,y = xy[0]
    if(x<=d):
        print(y)
    else:
        print(0)
    exit()

n1 = n//2
n2 = n-n1

xy1 = tuple(xy[:n1])
xy2 = tuple(xy[n1:])

def calc_g(n1,xy1):
    g1 = []
    for i in range(3**n1):
        dx,dy = 0,0
        j = 0
        while(i>0):
            if(i%3==1):
                dx += xy1[j][0]
                dy += xy1[j][1]
            elif(i%3==2):
                dx -= xy1[j][0]
                dy -= xy1[j][1]
            i //= 3
            j += 1
        if(dx >= 0):
            g1.append((dx,dy))
    return g1

g1 = calc_g(n1,xy1)
g2 = calc_g(n2,xy2)

g2.sort()
g2_x,g2_y = [],[]
for x,y in g2:
    g2_x.append(x)
    g2_y.append(y)

seg_max = Seg_max(g2_y)
seg_min = Seg_min(g2_y)

def get_segmax(n_min,n_max):
    left = bisect.bisect_left(g2_x,n_min)
    right = bisect.bisect_right(g2_x,n_max)
    return seg_max.query(left,right)

def get_segmin(n_min,n_max):
    left = bisect.bisect_left(g2_x,n_min)
    right = bisect.bisect_right(g2_x,n_max)
    return seg_min.query(left,right)

ans = 0
for x,y in g1:
    # +g1 +g2
    y_max = get_segmax(-d-x,d-x)
    ans = max(ans, x+y_max)

    # +g1 -g2
    y_min = get_segmin(x-d,x+d)
    ans = max(ans, y-y_min)

    # -g1 +g2
    y_max = get_segmax(x-d,x+d)
    ans = max(ans, -y+y_max)

    # -g1 -g2
    y_min = get_segmin(-d-x,d-x)
    ans = max(ans, -y-y_min)

print(ans)


'''

'''
