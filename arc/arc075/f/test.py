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

import itertools

# d = int(input())
# if d%9 != 0:
#     print(0)
#     exit()

def calc(d,l):
    res = 0
    l2 = l//2
    base = []
    p_base = []
    head = False
    for i in range(l2):
        b = pow(10,l-1-i) - pow(10,i)
        base.append(b)
        if head:
            p_base.append(list(range(-9,10)))
        else:
            if b > d*20:
                p_base.append([0])
            else:
                head = True
                p_base.append(list(range(-9,10)))

    if len(p_base[-1]) == 1:
        return 0
    
    for cand in itertools.product(*p_base):
        cand = list(cand)
        tot = 0
        cnt = 1 if l2*2 == l else 10
        for i in range(l2):
            tot += base[i] * cand[i]
            # if abs(tot - d) > base[i]:
            #     break
            if i == 0:
                cnt *= 9 - abs(cand[i])
            else:
                cnt *= 10 - abs(cand[i])
            print(l,i,tot,cnt,cand,base)
        else:
            if tot == d:
                res += cnt
    
    # print(base)
    # print(p_base)
    return res

def solve(d):
    ans = 0
    for i in range(2,22):
        res = calc(d,i)
        # print(i,res)
        ans += res

    # print(ans)
    return ans


print(solve(1989))

'''
9999 ,990

999, 90

99999,9990,900
89910

10089
 8100
 1989

l=6 (1,-9,-9)



'''


# simp = [0] * (10**6)
# for i in range(10**6):
#     rev = int(str(i)[::-1])
#     if rev >= i:
#         simp[rev-i] += 1
#         if rev-i == 189:
#             print(i)

# for i in range(1,1000):
#     res = solve(i)
#     if res != simp[i]:
#         print(i,simp[i],res)

'''
189

1902
2091

base = [999,90]
1,-9

'''