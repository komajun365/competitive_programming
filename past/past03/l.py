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
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
data = list(map(int,read().split()))

inf = 10**6 * -1
t = [[] for _ in range(n)]
i = 0
for j in range(n):
    k = data[i]
    t[j] =  [inf,inf] + data[i+1:i+1+k][::-1]
    i += 1+k
m = data[i]
a = data[i+1:]

class Seg_max():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 10**10 * -1
        self.func = max

        self.n = len(x)

        #num_max:n以上の最小の2のべき乗
        self.num_max =2**(self.n-1).bit_length()
        self.x = [[self.ide_ele_min, -1] for _ in range(2*self.num_max)]

        for i,num in enumerate(x, self.num_max):
            self.x[i][0] = num
            self.x[i][1] = i - self.num_max
        for i in range(self.num_max-1,0,-1):
            if(self.x[i<<1] > self.x[(i<<1) + 1]):
                self.x[i][0] = self.x[i<<1][0]
                self.x[i][1] = self.x[i<<1][1]
            else:
                self.x[i][0] = self.x[(i<<1) + 1][0]
                self.x[i][1] = self.x[(i<<1) + 1][1]

    def update(self,i,x):
        i += self.num_max
        self.x[i][0] = x
        while(i>0):
            i = i//2
            if(self.x[i<<1] > self.x[(i<<1) + 1]):
                self.x[i][0] = self.x[i<<1][0]
                self.x[i][1] = self.x[i<<1][1]
            else:
                self.x[i][0] = self.x[(i<<1) + 1][0]
                self.x[i][1] = self.x[(i<<1) + 1][1]

    def query(self,i,j):
        res = [self.ide_ele_min,-1]
        if i>=j:
            return res
        i += self.num_max
        j += self.num_max -1
        while(i<=j):
            if(i==j):
                if(self.x[i][0] > res[0]):
                    res[0] = self.x[i][0]
                    res[1] = self.x[i][1]
                break
            if(i&1):
                if(self.x[i][0] > res[0]):
                    res[0] = self.x[i][0]
                    res[1] = self.x[i][1]
                i += 1
            if(not j&1):
                if(self.x[j][0] > res[0]):
                    res[0] = self.x[j][0]
                    res[1] = self.x[j][1]
                j -= 1
            i = i>>1
            j = j>>1
        return res

t1 = [0] * n
t2 = [0] * n
for i in range(n):
    t1[i] = t[i].pop()
    t2[i] = t[i].pop()

seg1 = Seg_max(t1)
seg2 = Seg_max(t2)

ans = []
for i in a:
    if(i==1):
        num1,ind1 = seg1.query(0,n)
        ans.append(num1)
        next1,_ = seg2.query(ind1,ind1+1)
        seg1.update(ind1,next1)
        next2 =  t[ind1].pop()
        seg2.update(ind1,next2)
    else:
        num1,ind1 = seg1.query(0,n)
        num2,ind2 = seg2.query(0,n)
        if(num1 > num2):
            ans.append(num1)
            next1,_ = seg2.query(ind1,ind1+1)
            seg1.update(ind1,next1)
            next2 =  t[ind1].pop()
            seg2.update(ind1,next2)
        else:
            ans.append(num2)
            next2 =  t[ind2].pop()
            seg2.update(ind2,next2)

print('\n'.join(map(str,ans)))
