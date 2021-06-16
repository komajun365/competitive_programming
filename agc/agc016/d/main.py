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
a = list(map(int,input().split()))
b = list(map(int,input().split()))

xor_a = 0
for ai in a:
    xor_a ^= ai
xor_b = 0
for bi in b:
    xor_b ^= bi

a1 = a + [xor_a]
a1.sort()
b1 = b + [xor_b]
b1.sort()
if a1 != b1:
    print(-1)
    exit()

a.append(xor_a)
b.append(xor_b)

idx_a = dict()
for i,ai in enumerate(a):
    if ai in idx_a:
        idx_a[ai].append(i)
    else:
        idx_a[ai] = [i]

idx_b = dict()
for i,bi in enumerate(b):
    if bi in idx_b:
        idx_b[bi].append(i)
    else:
        idx_b[bi] = [i]

ans = 0
done = [0] * (n+1)
for i in range(n):
    if a[i] == b[i]:
        done[i] = 1
done[-1] = 1
done_num = set()
done_num.add(xor_a)
done_num.add(xor_b)
stack = list(done_num)

cnt = 0
while stack:
    i = stack.pop()
    for j in idx_a[i]:
        if done[j] == 1:
            continue
        done[j] = 1
        cnt += 1
        if b[j] in done_num:
            continue
        stack.append(b[j])
        done_num.add(b[j])
    for j in idx_b[i]:
        if done[j] == 1:
            continue
        done[j] = 1
        cnt += 1
        if a[j] in done_num:
            continue
        stack.append(a[j])
        done_num.add(a[j])

ans += cnt

for i in range(n):
    if done[i] == 1:
        continue
    
    done_num = set()
    done_num.add(a[i])
    done_num.add(b[i])
    stack = list(done_num)
    done[i] = 1

    cnt = 1
    while stack:
        i = stack.pop()
        for j in idx_a[i]:
            if done[j] == 1:
                continue
            done[j] = 1
            cnt += 1
            if b[j] in done_num:
                continue
            stack.append(b[j])
            done_num.add(b[j])
        for j in idx_b[i]:
            if done[j] == 1:
                continue
            done[j] = 1
            cnt += 1
            if a[j] in done_num:
                continue
            stack.append(a[j])
            done_num.add(a[j])

    ans += cnt+1

print(ans)