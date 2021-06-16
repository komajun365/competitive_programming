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
abcde - edcba = 9999*a + 990*b + c - c - 990*d - 9999*e
= 9999*(a-e) + 990*(b-d) + 1*(c-c)

10**9 -> 9ケタ
-9~9 で　19**4全探索できるか？

Nは10桁以上の可能性がある
いや、(a-z)の値は固定できそう。嘘。

abcdefghij
-> 999_999_999 * (a-j) + 
    99_999_990 * (b-i) + 
     9_999_900 * (c-h) + 
       999_000 * (d-g) + 
        90_000 * (e_f)


20桁以上にはならない。

'''

# import itertools

d = int(input())
if d%9 != 0:
    print(0)
    exit()

def calc(l):
    res = 0
    l2 = l//2
    base = []
    p_base = []
    head = False
    for i in range(l2):
        b = pow(10,l-1-i) - pow(10,i)
        base.append(b)
    
    def dfs(dep,tot):
        if dep == l2:
            if tot == d:
                if l != l2*2:
                    return 10
                else:
                    return 1
            else:
                return 0

        b = base[dep]
        if abs(tot-d) > b*10:
            return 0
        
        res = 0
        if dep == 0:
            for i in range(-8,9):
                res += dfs(dep+1, tot + i*b) * (9 - abs(i))
        else:
            for i in range(-9,10):
                res += dfs(dep+1, tot + i*b) * (10 - abs(i))
        
        return res
    
    res = dfs(0,0)
    return res

ans = 0
for i in range(2,20):
    res = calc(i)
    # print(i,res)
    ans += res

print(ans)

# calc(2)