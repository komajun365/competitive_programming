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
# f = open('../../input.txt', 'r')
# sys.stdin = f

# とりあえずtestset2まで

# import sys
# read = sys.stdin.read

n = 3
q = 6
s = ['TTFTFT', 'TTFTTF', 'TTTFFF']
a = [4,4,3]

s2 = []
for i in range(n):
    x = 0
    for j in range(q):
        x *= 2
        if s[i][j] == 'T':
            x += 1
    s2.append(x)

cand = []
for i in range(1<<q):
    for j in range(n):
        score = q
        x = i^s2[j]
        for k in range(q):
            if (x >> k) & 1:
                score -= 1
        if score != a[j]:
            break
    else:
        cand.append(i)

if len(cand) == 0:
    print('no cand')
    exit()

y = 0
for i in range(1<<q):
    tmp = 0
    for ci in cand:
        x = i^ci
        for k in range(q):
            if not (x >> k) & 1:
                tmp += 1
    if y < tmp:
        print(tmp,bin(i))
    y = max(y,tmp)

print(y,len(cand))




# x = 2901503505434414233388602018
# cnt = 0
# while x % 2==0:
#     x //= 2
#     cnt += 1
# print(cnt,x)





# t,*data = read().split()
# t = int(t)

# def solve(n,q,a,s):
#     # print(n,q)
#     # print(a)
#     # print(s)
#     if n == 1:
#         a = a[0]
#         s = s[0]
#         if s*2 >= q:
#             return a,s,1
#         y = ''
#         for ai in a:
#             if ai=='T':
#                 y += 'F'
#             else:
#                 y += 'T'
#         return y,q-s,1
    
#     if n == 2:
#         if s[0] < s[1]:
#             a = a[::-1]
#             s = s[::-1]
#         ns = 0
#         nm = 0
#         same = [0] * q
#         for i in range(q):
#             if a[0][i] == a[1][i]:
#                 same[i] = 1
#                 ns += 1
#             else:
#                 nm += 1

#         score_same = (sum(s) - nm) //2
#         if score_same*2 >= ns:
#              return a[0],s[0],1
        
#         z = s[0] - score_same + ns - score_same
#         y = ''
#         for i in range(q):
#             if same[i] == 1:
#                 if a[0][i] == 'T':
#                     y += 'F'
#                 else:
#                     y += 'T'
#             else:
#                 y += a[0][i]
#         return y,z,1

#     return 1,2,3

    
# ans = [''] * t
# idx = 0
# for i in range(t):
#     n = int(data[idx])
#     q = int(data[idx+1])
#     a = data[idx+2:idx+2+2*n:2]
#     s = [int(i) for i in data[idx+3:idx+3+2*n:2]]
#     idx += 2 + 2*n
#     y,z,w = solve(n,q,a,s)
#     ans[i] = 'Case #{}: {} {}/{}'.format(i+1,y,z,w)
# print('\n'.join(ans))

