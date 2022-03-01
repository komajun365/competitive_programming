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

base = 111111111

def calc(x):
    if x == 9:
        return 1000000000
    elif x > 9:
        x -= 1

    res = 0
    top = x // base
    res += top+1
    x %= base
    
    b = base
    while x != 0:
        x -= 1
        b //= 10
        top = x // b
        res = res*10 + top
        x %= b
    
    return res

# print('? 1000000000', flush=True)
# res1 = input()
# print('? 1000000001', flush=True)
# res2 = input()

# if res1 == 'Y' and res2 == 'N':
#     print('! 1000000000', flush=True)
#     exit()

def check(x):
    num = calc(x)
    print('? {}000000000'.format(num), flush=True)
    res = input()
    return res == 'Y'

ng = -1
ok = 1000000000
while ok-ng > 1:
    mid = (ng+ok)//2
    if check(mid):
        ok = mid
    else:
        ng = mid

ans = calc(ok)

while ans * 10 <= 10**9:
    if ans % 10 != 9:
        print('? {}'.format(ans + 1), flush=True)
        res = input()
        if res == 'Y':
            break
    else:
        print('? {}'.format(ans * 10 - 9), flush=True)
        res = input()
        if res == 'N':
            break
    ans *= 10


print('! {}'.format(ans), flush=True)
exit()








'''
13 130

99 990
981

'''


