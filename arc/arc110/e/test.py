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


# simple
def solve_simple(n,s):
    make = [set() for _ in range(n+1)]
    make[n].add(s)

    keys = ['AB', 'AC', 'BA', 'BC', 'CA', 'CB']
    vals = 'CBCABA'
    d = dict()
    for k,v in zip(keys, vals):
        d[k] = v
    
    for i in range(n,1,-1):
        for t in make[i]:
            for j in range(i-1):
                cut = t[j:j+2]
                if cut in d:
                    tmp = t[:j] + d[cut] + t[j+2:]
                    make[i-1].add(tmp)
    
    ans = 0
    for i in range(1,n+1):
        ans += len(make[i])
    
    return ans,make

for i in range(1,10):
    m = [0,'']
    for j in range(3**i):
        s = ''
        for _ in range(i):
            s += 'ABC'[j%3]
            j //= 3
        s = s[::-1]
        n = len(s)
        ans,make = solve_simple(n,s)
        # print(s,ans)
        if ans > m[0]:
            m[0] = ans
            m[1] = s
    print(m)
        




# s = 'ABCABC'
# n = len(s)

# ans,make = solve_simple(n,s)
# print(ans)
# for i in make:
#     print(i)