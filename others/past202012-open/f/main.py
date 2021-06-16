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

n,m,*data = map(int,read().split())
it = iter(data)
abc = [[a-1,b-1,c-1] for a,b,c in zip(it,it,it)]

def check(bi):
    cand = set()
    for a,b,c in abc:
        use = []
        not_use = []
        for x in [a,b,c]:
            if (bi >> x)&1:
                use.append(x)
            else:
                not_use.append(x)
        if len(use) == 3:
            return 0
        if len(not_use) == 1:
            cand.add(not_use[0])
    return len(cand)


ans = 0
for bi in range(1<<n):
    ans = max(ans, check(bi))
print(ans)