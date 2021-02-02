# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

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
c = list(map(int, readline().split()))
q = int(readline())
ss = [tuple(map(int,i.split())) for i in readlines()]

len_odd = (n+1)//2
len_even = n//2
c_odd = c[::2]
c_even = c[1::2]


class segtree:
    ini = 10**10
    num_max = 0
    val = []
    def __init__(self,n,c):
        self.num_max = 2**(len(str(bin(n-1))) -2)
        self.val = [[self.ini,0] for _ in range(self.num_max * 2)]
        for i,num in enumerate(c, self.num_max):
            self.val[i][0] = num
        for i in range(self.num_max-1, 0,-1):
            self.val[i][0] = min(self.val[i*2][0], self.val[i*2][0])

    def get_range(self,left,right):
        left += self.num_max
        right += self.num_max -1
        res = []
        while(left <= right):
            if(left==right):
                res.append(left)
                break
            if(left&1):
                res.append(left)
                left += 1
            left = left//2
            if(not (right&1)):
                res.append(right)
                right -=1
            right = right//2
        return res

    def add(self,left,right,num):
        ranges = self.get_range(left,right)
        for i in ranges:
            self.val[i][1] += num
        stack = set()
        for i in ranges:
            while(i > 0):
                stack.add(i)
                i = i//2
        stack = sorted(list(stack))
        for i in stack:
            if(i < self.num_max):
                self.val[i][0] = min(sum(self.val[i*2]),sum(self.val[i*2+1]))

    def done_add(self,i):
        num,a = self.val[i]
        self.val[i] = [num+a, 0]
        if(i < self.num_max):
            self.val[i*2][1] += a
            self.val[i*2+1][1] += a

    def get_min(self,left,right):
        ranges = self.get_range(left,right)
        stack = set()
        for i in ranges:
            while(i > 0):
                stack.add(i)
                i = i//2
        stack = sorted(list(stack))
        for i in stack:
            self.done_add(i)

        res = self.ini
        for i in ranges:
            res = min(res,self.val[i][0])
        return res

st_odd = segtree(len_odd,c_odd)
st_even = segtree(len_even,c_even)

ans = 0
for s in ss:
    if(s[0]==1):
        x,a = s[1:]
        x -= 1
        if(x%2==0):
            st = st_odd
        else:
            st = st_even
        x = x//2
        if(st.get_min(x,x+1) >= a):
            ans += a
            st.add(x,x+1,-1*a)
    elif(s[0]==2):
        a = s[1]
        if(st_odd.get_min(0,len_odd) >= a):
            ans += a * len_odd
            st_odd.add(0,len_odd,-1*a)
    elif(s[0]==3):
        a = s[1]
        buymax = min(st_odd.get_min(0,len_odd), st_even.get_min(0,len_even))
        if(buymax >= a):
            ans += a * n
            st_odd.add(0,len_odd,-1*a)
            st_even.add(0,len_even,-1*a)

print(ans)




# print(st.val)
# st.add(1,3,3)
# print(st.val)
# hoge = st.get_min(0,3)
# print(hoge)
# print(st.val)
