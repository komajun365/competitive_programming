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

k,m = map(int,input().split())

ans = -1
if k < 10**5:
    if m == 10**10:
        if 10 ** 10 % k == 1:
            ans += 1
        m -= 1
    head = m // (10**5)
    tail = m % (10**5)

    rem_h = [0] * k
    rem_t = [0] * k
    for i in range(10**5):
        n = i
        tot = 0
        while n > 0:
            tot += n % 10
            n //= 10
        rem_t[(i - tot)% k] += 1
        if i < head:
            rem_h[(i*(10**5) - tot)% k] += 1
    for i in range(k):
        ans += rem_h[i] * rem_t[-i]
    for i in range(m-tail,m+1):
        n = i
        tot = 0
        while n > 0:
            tot += n % 10
            n //= 10
        if (i-tot) % k == 0:
            ans += 1
else:
    for x in range(0,m+1,k):
        for y in range(91):
            n = x + y
            if y > m:
                break
            tot = 0
            while n > 0:
                tot += n % 10
                n //= 10
            if tot % k == y:
                ans += 1

print(ans)


