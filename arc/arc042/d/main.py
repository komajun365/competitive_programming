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

x,p,a,b = map(int,input().split())

if b - a < 10**7:
    ans = p
    tmp = pow(x,a,p)
    for _ in range(b-a+1):
        ans = min(ans,tmp)
        tmp = tmp * x % p
    print(ans)
    exit()

l = 10**6
head = (b-a+1) % l
ans = p
tmp = pow(x,a,p)
for _ in range(head):
    ans = min(ans,tmp)
    tmp = tmp * x % p

a += head
base = []
for i in range(a,b,l):
    base.append( pow(x,i,p) )

ex = set()
tmp = 1
for i in range(l):
    ex.add(tmp)
    tmp = tmp * x % p

for i in range(1, ans):
    for j in range(len(base)):
        rev = pow(base[j], p-2, p) * i % p
        if rev in ex:
            print(i)
            exit()

print(ans)


'''
x * y = a
y = x^-1 * a

'''


'''
x^i = y (mod p)

x^1 ~ x^(b-a)**0.5

'''