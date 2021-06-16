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

p,a,b = map(int,input().split())

a_ex = [1]
b_ex = [1]
for _ in range(p):
    cand = a_ex[-1] * a % p
    if cand == 1:
        break
    a_ex.append(cand)

for _ in range(p):
    cand = b_ex[-1] * b % p
    if cand == 1:
        break
    b_ex.append(cand)

if len(a_ex) == p-1:
    a_ex.append(1)
    print('Yes')
    print(' '.join(map(str,a_ex)))
    exit()

if len(b_ex) == p-1:
    b_ex.append(1)
    print('Yes')
    print(' '.join(map(str,b_ex)))
    exit()

# a_set = set(a_ex)
# b_set = set(b_ex)
# if a in b_set and b in a_set:
#     print('No')
#     exit()

def solve(a,b,a_ex,b_ex):
    nums = [a_ex[::]]
    for i in range(1,(p-1)//len(a_ex)):
        nums.append([])
        for j in range(len(a_ex)):
            nums[i].append(nums[i-1][j] * b % p)

    x = len(a_ex)
    y = len(nums)

    ans = []
    if y % 2 == 0:
        for i in range(y):
            ans.append(nums[i][0])
        for i in range(y-1,-1,-1):
            if i % 2 == 1:
                for j in range(1,x):
                    ans.append(nums[i][j])
            else:
                for j in range(x-1,0,-1):
                    ans.append(nums[i][j])
    elif x % 2 == 0:
        for j in range(x):
            if j % 2 == 0:
                for i in range(y):
                    ans.append(nums[i][j])
            else:
                for i in range(y-1,-1,-1):
                    ans.append(nums[i][j])
    else:
        for i in range(y):
            ans.append(nums[i][0])
        for j in range(1,x):
            ans.append(nums[-1][j])
        
        for i in range(y-2,-1,-1):
            if i % 2 == 0:
                for j in range(1,x):
                    ans.append(nums[i][j])
            else:
                for j in range(x-1,0,-1):
                    ans.append(nums[i][j])

    check = [0] * p
    for i in ans:
        if check[i] == 0:
            check[i] = 1
        else:
            # print('No')
            # exit()
            return False

    ans.append(1)
    print('Yes')
    print(' '.join(map(str,ans)))
    exit()

solve(a,b,a_ex,b_ex)
solve(b,a,b_ex,a_ex)
print('No')


