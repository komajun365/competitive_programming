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

'''
条件３の長さをxとおく。
xは二分探索で求まる。

A*？、B＊？をそれぞれ(A)(B)とする。
辞書順最小の文字列は
・(B)(A)...(A)(B)
→　頭にAが置けないケース。(A)は全部1文字。
　　先頭の（B)をなるべく短くする。
・(A)(B)...(B)(A)
→　最後にBが置けないケース。(B)は全部1文字。
　最後の(A)をなるべく短くする。
を除くと
・(A)B(A)...(A)(B)A(B)A(B)...A(B)
　になる。このとき頭の方の(A) とおしりの方の（B）はなるべくx文字。
　これは、頭のブロックがいくつ置けるかをさらに二分探索すれば最終形が求まる。

8,10
AABAABABBABBABBABB


'''
import sys
read = sys.stdin.buffer.read

q,*abcd = map(int,read().split())

def canmake(x,a,b):
    a_min = -(-a // x)
    b_min = -(-b // x)
    if a + 1 < b_min:
        return False
    if b + 1 < a_min:
        return False
    return True

def canmake_a(x,a,b):
    if a < 0 or b < 0:
        return False
    # 先頭はA
    a_min = -(-a // x)
    b_min = -(-b // x)
    if a < b_min:
        return False
    if b + 1 < a_min:
        return False
    return True

def calc(x,a,b,c,d):
    a_min = -(-a // x)
    b_min = -(-b // x)
    if b_min > a:
        head = b - x*a
        res = ''
        for i in range(c,d+1):
            if i <= head:
                res += 'B'
            else:
                if (i - head) % (1+x) == 1:
                    res += 'A'
                else:
                    res += 'B'
        return res
    
    if a_min > b:
        tail = a - x*b
        head = a+b-tail
        res = ''
        for i in range(c,d+1):
            if i <= head:
                if i % (1+x) == 0:
                    res += 'B'
                else:
                    res += 'A'
            else:
                res += 'A'
        return res
    
    ok = 0
    ng = (a // x) + 1
    while ng-ok > 1:
        mid = (ng+ok)//2
        a2 = a - mid*x
        b2 = b - mid
        if canmake_a(x,a2,b2):
            ok = mid
        else:
            ng = mid
    
    head = (x+1) * ok
    a2 = a - ok*x
    b2 = b - ok
    tail = min(b2//x, a2)
    a3 = a2 - tail
    b3 = b2 - tail*x
    tail *= (1+x)
    body = a+b-tail
    res = ''
    for i in range(c,d+1):
        if i <= head:
            if i % (1+x) == 0:
                res += 'B'
            else:
                res += 'A'
        elif i > body:
            if (i-body) % (x+1) == 1:
                res += 'A'
            else:
                res += 'B'
        else:
            if i-head <= a3:
                res += 'A'
            else:
                res += 'B'
    return res
    



ans = []
it = iter(abcd)
for a,b,c,d in zip(it,it,it,it):
    ok = max(a,b)
    ng = 0
    while ok - ng > 1:
        mid = (ok+ng)//2
        if canmake(mid,a,b):
            ok = mid
        else:
            ng = mid
    
    x = ok
    ans.append(calc(x,a,b,c,d))

# print(ans)
print('\n'.join(ans))


