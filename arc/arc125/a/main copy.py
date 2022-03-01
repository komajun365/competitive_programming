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

n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if sum(a) == 0 and sum(b) > 0:
    print(-1)
    exit()
elif sum(a) == n and sum(b) == 0:
    print(-1)
    exit()
elif a[0] == 0 and sum(b) == 0:
    print(m)
    exit()
elif a[0] == 1 and sum(b) == m:
    print(m)
    exit()

ans = 10**10
a2 = a + a
for i in range(n):
    if a2[i] != a2[i+1]:
        ans = min(ans, i)
        break
for i in range(0,-n,-1):
    if a2[i] != a2[i-1]:
        ans = min(ans, -i)
        break

now = a[0]
for bi in b:
    if now == bi:
        ans += 1
    else:
        ans += 2
        now = 1-now
print(ans)



# def calc(x, step):
#     idx = n
#     cnt = 0
#     for bi in b:
#         while x[idx] != bi:
#             if x[idx - step] == bi:
#                 cnt += 1
#                 idx -= step
#                 break
#             cnt += 1
#             idx += step
#         cnt += 1
#     return cnt

# ans = 10**10
# a2 = a + a + a + a
# ans = min(ans, calc(a2,1))
# ans = min(ans, calc(a2,-1))

# print(ans)