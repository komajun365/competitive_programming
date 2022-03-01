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

print('? 1000000000', flush=True)
res1 = input()
print('? 1000000001', flush=True)
res2 = input()

if res1 == 'Y' and res2 == 'N':
    print('! 1000000000', flush=True)
    exit()

def check(x):
    num = calc(x)
    print('? {}000000000'.format(num), flush=True)
    res = input()
    return res == 'Y'

ok = 0
ng = 1000000000
while ng-ok > 1:
    mid = (ng+ok)//2
    if check(mid):
        ng = mid
    else:
        ok = mid

print('! {}'.format(calc(ok+1)), flush=True)
exit()











