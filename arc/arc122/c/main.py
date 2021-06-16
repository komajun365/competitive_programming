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

n = int(input())

if n <= 130:
    print(n)
    for i in range(n):
        print(1)
    exit()

x = n
y = round(x * 2 / (1 + 5**0.5))
ans = []
rem = 130
cyc = 0
while x + y > rem:
    if x > y:
        if x % y == 0:
            x -= 1
            ans.append(1)
        else:
            x -= y
            ans.append(3)
    else:
        if y % x == 0:
            y -= 1
            ans.append(2)
        else:
            y -= x
            ans.append(4)

    rem -= 1
    if rem == 0:
        x = n
        cyc += 1
        y = round(x * 2 / (1 + 5**0.5)) + cyc
        rem = 130
        ans = []

for i in range(x):
    ans.append(1)
for i in range(y):
    ans.append(2)

ans = ans[::-1]
print(len(ans))
print('\n'.join(map(str,ans)))
