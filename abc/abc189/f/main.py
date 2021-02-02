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

class SegTree:
    def __init__(self, op, e, n: int = -1, v: list = []):
        assert (len(v) > 0) | (n > 0)
        if(len(v) == 0):
            v = [e()] * n
        self.__n = len(v)
        self.__log = (self.__n - 1).bit_length()
        self.__size = 1 << self.__log
        self.__d = [e()] * (2 * self.__size)
        self.__op = op
        self.__e = e
        for i in range(self.__n):
            self.__d[self.__size + i] = v[i]
        for i in range(self.__size - 1, 0, -1):
            self.__update(i)

    def __update(self, k: int):
        self.__d[k] = self.__op(self.__d[2 * k], self.__d[2 * k + 1])

    def set(self, p: int, x):
        assert (0 <= p) & (p < self.__n)
        p += self.__size
        self.__d[p] = x
        for i in range(1, self.__log + 1):
            self.__update(p >> i)

    def get(self, p: int):
        assert (0 <= p) & (p < self.__n)
        return self.__d[p + self.__size]

    def prod(self, l: int, r: int):
        assert (0 <= l) & (l <= r) & (r <= self.__n)
        sml = self.__e()
        smr = self.__e()
        l += self.__size
        r += self.__size

        while(l < r):
            if(l & 1):
                sml = self.__op(sml, self.__d[l])
                l += 1
            if(r & 1):
                r -= 1
                smr = self.__op(self.__d[r], smr)
            l //= 2
            r //= 2

        return self.__op(sml, smr)

    def all_prod(self):
        return self.__d[1]
    
    def print(self):
        print(self.__d)

n,m,k = map(int,input().split())
if k==0:
    a = set()
else:
    a = set(map(int,input().split()))

def op(a,b):
    return [a[0] + b[0], a[1] + b[1]]

def e():
    return [0.0,0.0]

st = SegTree(op=op,e=e,n=n)
st.set(0,[1.0,0.0])
back = []

goal = [0.0,0.0]
if (n <= m):
    goal[0] += 1.0 * (m-n + 1)/m
    goal[1] += goal[0]


for i in range(1,n):
    prob,ex = st.prod(max(0,i-m),i)
    prob /= m
    ex /= m
    ex += prob

    if i in a:
        back.append([i,prob,ex])
    else:
        st.set( i, [prob,ex])
        
        rem = n-i
        if rem <= m:
            goal[0] += prob * (m-rem + 1)/m
            goal[1] += (ex + prob) * (m-rem + 1)/m 


if goal[0] < 10**-6:
    print(-1)
    exit()

goal[1] /= goal[0]

ex0 = 0.0
for bi in back:
    ex0 += bi[2]

ex0 /= goal[0]

print( ex0 + goal[1])
# st.print()
# print(goal)




