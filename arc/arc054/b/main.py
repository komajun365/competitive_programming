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

p = float(input())

def calc(x):
    if x > 90:
        res = x
    else:
        res = x + p/(2**(x/1.5))
    return res

left = 0
right = p
for _ in range(10000):
    m1 = left + (right-left)/3
    m2 = left + 2*(right-left)/3
    t1 = calc(m1)
    t2 = calc(m2)
    if t1 < t2:
        right = m2
    else:
        left = m1

print(calc(left))


