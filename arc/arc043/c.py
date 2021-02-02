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

class Seg_sum():
    def __init__(self,x):
        #####単位元######
        self.ide_ele_min = 0
        self.func = lambda a,b : a+b

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

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

b_ind = [0] * (n+1)
for i,bi in enumerate(b):
    b_ind[bi] = i

a2 = [0]*n
for i,ai in enumerate(a):
    a2[i] = b_ind[ai]

st = Seg_sum([0]*n)
tn = 0
for ai in a2:
    tn += st.query(ai,n+1)
    st.update(ai,1)

if(tn%2==1):
    print(-1)
    exit()

tn //= 2

ans = []
st = Seg_sum([1]*n)
for i,ai in enumerate(a2):
    max_tn = st.query(0,ai)
    if(tn > max_tn):
        ans.append(ai)
        tn -= max_tn
        st.update(ai,0)
        continue
    else:
        x = st.x[st.num_max: st.num_max+n]
        x[ai] = 0
        tmp=max_tn-tn
        for i,xi in enumerate(x):
            if(xi==1):
                ans.append(i)
                tmp -= 1

            if(tmp==0):
                ans.append(ai)
                tmp -= n
        break

ans2 = [0] * n
for i,ai in enumerate(ans):
    ans2[i] = b[ai]

print(' '.join(map(str,ans2)))

# print(ans)
# print(a2)
# print(ans)
# print(ans2)


'''
まずは転倒数

3,1,4,2,5-2,5,3,4,1

3,5,4,1,2




どっちかを1,2,...,nにして
転倒数を調べる。
偶数なら半分にすればよい。


'''
