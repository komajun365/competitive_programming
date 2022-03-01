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

# 嘘解法なので落ちる

n = int(input())
a = list(map(int,input().split()))

l = -1 * 10**15
r = 10 ** 15

def calc(x):
    bi = x
    ci = a[0] - bi
    res = abs(bi) + abs(ci)

    for i in range(1,n):
        dif = a[i] - a[i-1]
        if dif > 0:
            bi += dif
        else:
            ci += dif
        res += abs(bi) + abs(ci)
    return res

lc = calc(l)
rc = calc(r)

while r - l > 5:
    m1 = l + (r-l)//3
    m2 = r - (r-l)//3
    m1c = calc(m1)
    m2c = calc(m2)

    if m1c < m2c:
        r = m2
        rc = m2c
    elif m1c > m2c:
        l = m1
        lc = m1c
    else:
        
    
ans = 10**18
for i in range(l,r+1):
    # print(i,calc(i))
    ans = min(ans, calc(i))
print(ans)


