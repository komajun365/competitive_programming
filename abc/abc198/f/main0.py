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

s = int(input())
mod = 998244353

def matmul(x,y):
    size = len(x)
    res = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                res[i][j] += x[i][k] * y[k][j]
            res[i][j] %= mod
    return res

# def calc3(a,b,c):


s -= 6
c111111 = 1
for i in range(1,6):
    c111111 *= s+6-i
    c111111 //= i
c111111 %= mod

c6 = (s % 6 == 0)*1
c33 = 0
if s % 3 == 0:
    c33 = (s//3 +1) % mod

c24 = 0
if s % 2 == 0:
    s2 = s//2
    c24 = (s2//2 +1) % mod

c15 = (s//5 + 1) % mod

# c411
head = s%4 + 1
tail = s+1
c411 = (head+tail) * ((tail-head)//4 + 1) //2  % mod

c222 = 0
if s % 2 == 0:
    s2 = s//2
    c222 = 1
    for i in range(1,3):
        c222 *= s2+3-i
        c222 //= i

c321 = 0
tail1 = s+1
tail2 = s-3
head1 = (s+1) % 6
head2 = (head1 + 3) % 6
if head1 % 2 == 0:
    head1,head2 = head2,head1
if tail1 % 2 == 0:
    tail1,tail2 = tail2,tail1
head1 //= 2
head2 //= 2
tail1 //= 2
tail2 //= 2
if head1 >= 0 and tail1 >= 0:
    c321 += (head1+tail1) * ((tail1-head1)//3 + 1) //2  % mod
if head2 >= 0 and tail2 >= 0:
    c321 += (head2+tail2) * ((tail2-head2)//3 + 1) //2  % mod
print(head1,tail1,head2,tail2)

print(c111111)
print(c15,c24,c33)
print(c411,c222,c321)
print(c6)