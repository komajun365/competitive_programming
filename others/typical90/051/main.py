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

n,k,p = map(int,input().split())
a = list(map(int,input().split()))

if n == 1:
    ans = 1 * (a[0] <= p)
    print(ans)
    exit()

n1 = n//2
n2 = n-n1
a1 = a[:n1]
a2 = a[n1:]

def search(x):
    res = [[] for _ in range(k+1)]
    res[0] = [0]
    for xi in x:
        for i in range(k,0,-1):
            tmp = []
            l1 = len(res[i-1])
            l2 = len(res[i])
            i1 = 0
            i2 = 0
            while i1 < l1 or i2 < l2:
                if i1 == l1:
                    tmp.append(res[i][i2])
                    i2 += 1
                elif i2 == l2:
                    tmp.append(res[i-1][i1] + xi)
                    i1 += 1
                else:
                    if res[i][i2] > res[i-1][i1] + xi:
                        tmp.append(res[i-1][i1] + xi)
                        i1 += 1
                    else:
                        tmp.append(res[i][i2])
                        i2 += 1
            res[i] = tmp
    return res

ans = 0
res1 = search(a1)
res2 = search(a2)
for i in range(k+1):
    j = k-i
    l1 = len(res1[i])
    l2 = len(res2[j])
    i2 = l2-1
    for i1 in range(l1):
        while i2 >= 0:
            if res1[i][i1] + res2[j][i2] <= p:
                break
            i2 -= 1
        ans += i2+1
print(ans)



