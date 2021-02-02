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

import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

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

h,w,m = map(int,readline().split())
if(m == 0):
    print(h*w)
    exit()
xy0 = list(map(int,read().split()))

it = iter(xy0)
stone = [[] for _ in range(h)]
for x,y in zip(it,it):
    x -= 1
    y -= 1
    stone[x].append(y)

def op(x,y):
    return x+y
def e():
    return 0

r = w
if(stone[0]):
    r = min(stone[0])
v = [1] * r + [0] * (w-r)

st = SegTree(op=op, e=e, v = v)
ans = 0
down = True
for i in range(h):
    if(down) and len(stone[i]) == 0:
        ans += w
        continue
    if(down):
        l = min(stone[i])
        if(l == 0):
            down = False
        else:
            for j in stone[i]:
                st.set(j, 0)
            ans += l + st.prod(l,w)
            continue
    for j in stone[i]:
        st.set(j, 0)
    ans += st.all_prod()

print(ans)



