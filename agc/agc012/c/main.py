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
cap = 1000

def make(m,use):
    l = 0
    x = m + 1
    while x > 0:
        l += 1
        x //= 2

    x = m + 1 - 2**(l-1)

    coms = [1]
    for i in range(l):
        tmp = coms[-1] * (l-i) // (i+1)
        if tmp <= coms[-1]:
            break
        coms.append(tmp)
    
    cl = len(coms)
    add = []
    for i in range(cl)[::-1]:
        ci = coms[i]
        while x >= ci:
            add.append(i)
            x -= ci
        
        if x < cap:
            break
    
    head = []
    body = [[] for _ in range(l)]
    while add:
        j = add.pop()
        head.append(use)
        body[j].append(use)
        use += 1
    
    res = head[::-1]
    for i in range(l):
        res += body[i]
        res += [use]
    use += 1
    return res,x,use

res,x,use = make(n,1)

for i in range(10,0,-1):
    j = 2**i-1
    while x >= j:
        res += [use] * (i+1)
        use += 1
        x -= j

print(len(res))
print(*res, sep=' ')



    





'''
abcde abcde = 2**5-1
abcde abced = 2**5-1 - 2**3

abcdef abcfde = 2**6-1 - 

'''





# def make(x,use):
#     head = []
#     tail = []
#     if x % 2 == 1:
#         head = [use]
#         tail = [use]
#         use += 1
#         x -= 1
    
#     cnt = 0
#     while x % 2== 0 and x != 0:
#         x //= 2
#         cnt += 1
    
#     if x == 1:
#         return head + [use] * (cnt+1) + tail
#     else:
#         next = make(x,use+1)
#         return head + [use] * (cnt+1) + next + tail

# ans = make(n+1, 1)
# print(len(ans))
# print(*ans, sep=' ')
