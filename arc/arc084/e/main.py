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

k,n = map(int,input().split())

def calc(k,n,x):
    # k**n が6*10**10以下のとき、x番目を返す
    one = 0
    for i in range(n):
        one += k**i
    
    top = (x-1) // one + 1
    x -= (top-1) * one + 1
    if x == 0:
        return [top]
    else:
        return [top] + calc(k,n-1,x)

if k == 1:
    x = (n+1)//2
    ans = [1] * x
    print(*ans)
    exit()
elif k % 2 == 0:
    ans = [k//2] + [k] * (n-1)
    print(*ans)
    exit()

cnt = [k]
while cnt[-1] < 10**11:
    cnt.append((cnt[-1]+1)*k)

l = len(cnt)
ans = []
m = n
while m > l:
    ans.append((k+1)//2)
    m -= 1

x = (cnt[m-1] + (n-m) + 1)//2 - (n-m)
ans += calc(k, m, x)
print(*ans)


    
'''
3 3 10
1,3,9

top = 1
x = 10

3 2 9
1,3
top = 3
x = 1


1
1 1
1 1 1
1 1 2
1 1 3

1 2
1 2 1
1 2 2
1 2 3
1 3

=====
5 40
[3] * 37
37 + 155 = 192
96-37 = 59番目

59 - 31 - 1 = 27
2

27 - 6*4 - 1 = 2
2 5 2

'''