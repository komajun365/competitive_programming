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

import sys
read = sys.stdin.buffer.read

def calc(n2,n3,n4):
    res = 0
    # 3*2+4*1
    x = min(n3//2, n4)
    res += x
    n3 -= x*2
    n4 -= x
    # 3*2+2*2
    x = min(n3//2, n2//2)
    res += x
    n2 -= x*2
    n3 -= x*2
    # 4*2+2*1
    x = min(n4//2,n2)
    res += x
    n2 -= x
    n4 -= x*2

    rem = (n4%2)*4 + n2*2
    res += rem//10
    return res

t,*case = map(int,read().split())
ans = []
it = iter(case)
for n2,n3,n4 in zip(it,it,it):
    ans.append(calc(n2,n3,n4))

print('\n'.join(map(str,ans)))

'''


'''