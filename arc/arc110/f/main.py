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

# class FenwickTree:
#     def __init__(self, n: int, mod: int = 0):
#         self.__mod = mod
#         self.__n = n
#         self.__data = [0] * self.__n

#     def add(self, p: int, x: int):
#         assert (0 <= p) & (p < self.__n)
#         if(self.__mod == 0):
#             self.__add_mod0(p, x)
#         else:
#             self.__add_mod(p, x)

#     def __add_mod0(self, p: int, x: int):
#         p += 1
#         while(p <= self.__n):
#             self.__data[p - 1] += x
#             p += p & -p

#     def __add_mod(self, p: int, x: int):
#         p += 1
#         while(p <= self.__n):
#             self.__data[p - 1] += x
#             self.__data[p - 1] %= self.__mod
#             p += p & -p

#     def sum(self, l: int, r: int):
#         assert (0 <= l) & (l <= r) & (r <= self.__n)
#         if(self.__mod == 0):
#             return self.__sum_mod0(r) - self.__sum_mod0(l)
#         else:
#             return (self.__sum_mod(r) - self.__sum_mod(l)) % self.__mod

#     def __sum_mod0(self, r: int):
#         s = 0
#         while(r > 0):
#             s += self.__data[r - 1]
#             r -= r & -r
#         return s

#     def __sum_mod(self, r: int):
#         s = 0
#         while(r > 0):
#             s += self.__data[r - 1]
#             s %= self.__mod
#             r -= r & -r
#         return s

# # 計算量オーダーは n = len(a),m= max(a)としてO(nlogm)
# def calc_invs(a):
#     m = max(a)
#     bit = FenwickTree(m+1)
#     res = 0
#     for i,ai in enumerate(a):
#         bit.add(ai,1)
#         res += i + 1 - bit.sum(0,ai+1)
#     return res

n = int(input())
p = list(map(int,input().split()))

if n == 2:
    if p[0] == 0:
        print(0)
        exit()
    else:
        print(1)
        print(0)
        exit()
elif n == 3:
    ans = []
    if p == [0,2,1]:
        ans = [1]
    elif p == [1,0,2]:
        ans = [0]
    elif p == [1,2,0]:
        ans = [0,0]
    elif p == [2,0,1]:
        ans = [2,1]
    elif p == [2,1,0]:
        ans = [0]
    print(len(ans))
    if len(ans) > 0:
        print('\n'.join(map(str,ans)))
    exit()

m1,m2 = 0,0
for i in range(n):
    if p[i] == n-1:
        m1 = i
    elif p[i] == n-2:
        m2 = i

ans = []
cnt = 0

def move_m1(m1,m2):
    p[(m1-1)%n], p[m1] = p[m1],p[(m1-1)%n]
    ans.append(m1)
    m1 = (m1-1) % n
    return m1,m2

# a,-2,-1 -> -2,-1,a
def move_m12(m1,m2):
    a = (m2-1)%n
    p[a],p[m2],p[m1] = p[m2],p[m1],p[a]
    ans.append(m1)
    ans.append(m1)
    m2,m1 = a,m2
    return m1,m2

# a,b,-2,-1 -> -2,-1,b,a
def move_inv(m1,m2):
    a = (m2-2)%n
    b = (m2-1)%n
    p[a],p[b],p[m2],p[m1] = p[m2],p[m1],p[b],p[a]
    ans.append(m2)
    ans.append(m1)
    ans.append(m2)
    m2,m1 = a,b
    return m1,m2

cnt0 = 0

while (m1-m2) % n != 1:
    cnt0 += 1
    m1,m2 = move_m1(m1,m2)

while cnt < n+10:
    cnt0 += 1
    # if cnt0 > 30:
    #     exit()
    # print(p)
    a = (m2-2)%n
    b = (m2-1)%n
    if p[a] < p[b] or (p[a] == n-3 and p[b] == 0):
        m1,m2 = move_m12(m1,m2)
        cnt += 1
    else:
        m1,m2 = move_inv(m1,m2)
        cnt = 0

while p[(m1+1)%n] != 0:
    m1,m2 = move_m12(m1,m2)

while p[0] != 0 or p[m1] != n-1:
    m1,m2 = move_m1(m1,m2)

print(len(ans))
if len(ans) > 0:
    print('\n'.join(map(str,ans)))

# print(p)



# print(p)
# m1,m2 = move_m1(m1,m2)
# m1,m2 = move_m1(m1,m2)
# print(p)

# inv = calc_invs(p)


'''
・-1が-2の隣に行く　：　n回
・バブルソートする　：　n**2*3???
・-2を0の近くに持ってく：　n回
・場所の調整　：　n**2



'''