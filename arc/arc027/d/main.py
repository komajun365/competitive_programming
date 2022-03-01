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

mod = 10**9 + 7

# 行列積
def mat_mul(x,y,l):
    res = [0] * l**2
    for i in range(l):
        for j in range(l):
            for k in range(l):
                res[i*l+j] += x[i*l+k] * y[k*l+j]
                res[i*l+j] %= mod
    return res

import sys
read = sys.stdin.buffer.read


n,*data = map(int,read().split())
h = data[:n]
d = data[n]
st = data[n+1:]

points = list(set(st))
points.sort()
encode = dict()
for i,pi in enumerate(points):
    encode[pi] = i

st2 = [encode[i] for i in st]
n2 = len(points)-1
tree_log = (n2 - 1).bit_length() + 1
n_tree = 2 ** tree_log 
tree = [[0] * 100 for _ in range(n_tree)]

e = [0] * 100
for i in range(10):
    e[i*10+i] = 1
e2 = [0] * 100
for i in range(1,10):
    e2[i*10+i-1] = 1

for i in range(n2):
    left = points[i]-1
    right = points[i+1]-1
    # print(n_tree//2 + i, n_tree, n2, i)
    tree[n_tree//2 + i] = e[::]
    for j in range(left+1,right+1):
        mat2 = e2[::]
        for k in range(1,11):
            if j - k < 0:
                break
            if h[j-k] >= k:
                mat2[k-1] = 1
        tree[n_tree//2 + i] = mat_mul(mat2,tree[n_tree//2 + i],10)

for i in range(n2, n_tree//2):
    tree[n_tree//2 + i] = e[::]

for i in range(n_tree//2-1,0,-1):
    tree[i] = mat_mul(tree[i*2+1],tree[i*2],10)


def calc(x,y):
    # x -> y
    res_l = e[::]
    res_r = e[::]
    x += n_tree//2
    y += n_tree//2
    while x < y:
        if x & 1:
            res_l = mat_mul(tree[x], res_l, 10)
            x += 1
        if y & 1:
            y -= 1
            res_r = mat_mul(res_r,tree[y], 10)
        x //= 2
        y //= 2

    return mat_mul(res_r,res_l, 10)

ans = []
it = iter(st2)
for s,t in zip(it,it):
    # print(s,t)
    res = calc(s,t)
    # print(s,t,res)
    ans.append(res[0])
print('\n'.join(map(str,ans)))


    

# print(tree[5])


# for i in range(n_tree//2,n_tree):
#     print(tree[i])
    

# print(mat_mul([1,2,3,4],[1,2,1,2],2))


