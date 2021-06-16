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
s = list(map(int,input().split()))
t = list(map(int,input().split()))
u = list(map(int,input().split()))
v = list(map(int,input().split()))

if n==1:
    if u[0] == v[0]:
        print(u[0])
    else:
        print(-1)
    exit()


def calc(ui,vi):
    cap0 = [[],[]] #0が1個以上
    cap1 = [[],[]] #要素1で確定
    cup0 = [[],[]] #要素0で確定
    cup1 = [[],[]] #1が1個以上
    for i,x,y in zip([0,1],[s,t],[ui,vi]):
        for j in range(n):
            if x[j] == 0 and y[j] == 0:
                cap0[i].append(j)
            elif x[j] == 0 and y[j] == 1:
                cap1[i].append(j)
            elif x[j] == 1 and y[j] == 0:
                cup0[i].append(j)
            else:
                cup1[i].append(j)
    
    # ng case
    if (len(cap1[0]) > 0 and len(cup0[1]) > 0) or \
       (len(cap1[1]) > 0 and len(cup0[0]) > 0):
        print(-1)
        exit()
    
    if len(cap1[0]) > 0 and len(cap1[1]) > 0:
        res = [[0] * n for _ in range(n)]
        for i in cap1[0]:
            for j in range(n):
                res[i][j] = 1
        for j in cap1[1]:
            for i in range(n):
                res[i][j] = 1
        return res
    
    if len(cup0[0]) > 0 and len(cup0[1]) > 0:
        res = [[1] * n for _ in range(n)]
        for i in cup0[0]:
            for j in range(n):
                res[i][j] = 0
        for j in cup0[1]:
            for i in range(n):
                res[i][j] = 0
        return res

    if len(cap1[0]) == 0 and len(cap1[1]) == 0 and \
       len(cup0[0]) == 0 and len(cup0[1]) == 0:
        res = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if (i+j) % 2 == 1:
                    res[i][j] = 1
        return res
    
    trans = 0
    if len(cap1[1]) + len(cup0[1]) > 0:
        trans = 1
        cap0 = cap0[::-1]
        cap1 = cap1[::-1]
        cup0 = cup0[::-1]
        cup1 = cup1[::-1]
    
    # len(cap1[0]) + len(cup0[0]) > 0
    if len(cap1[0]) > 0 and len(cup0[0]) > 0:
        res = [[0] * n for _ in range(n)]
        for x,num in zip([cap0,cap1,cup0,cup1],[0,1,0,1]):
            for i in x[0]:
                for j in range(n):
                    res[i][j] = num
    elif len(cap1[0]) > 0:
        if len(cap1[0]) == n-1:
            res = [[1] * n for _ in range(n)]
            if cap0[0]:
                rem,rem_num = cap0[0][0],0
            else:
                rem,rem_num = cup1[0][0],1
            cnt = [0,0]
            for x,num in zip([cap0,cup1],[0,rem_num]):
                for j in x[1]:
                    res[rem][j] = num
                    cnt[num] += 1
            if cnt[rem_num] == 0:
                print(-1)
                exit()
        else:
            res = [[1] * n for _ in range(n)]
            rem = cap0[0] + cup1[0]
            for i in range(len(rem)):
                for j in range(n):
                    res[rem[i]][j] = (i+j)%2
    elif len(cup0[0]) > 0:
        if len(cup0[0]) == n-1:
            res = [[0] * n for _ in range(n)]
            if cap0[0]:
                rem,rem_num = cap0[0][0],0
            else:
                rem,rem_num = cup1[0][0],1
            cnt = [0,0]
            for x,num in zip([cap0,cup1],[rem_num,1]):
                for j in x[1]:
                    res[rem][j] = num
                    cnt[num] += 1
            if cnt[rem_num] == 0:
                print(-1)
                exit()
        else:
            res = [[0] * n for _ in range(n)]
            rem = cap0[0] + cup1[0]
            for i in range(len(rem)):
                for j in range(n):
                    res[rem[i]][j] = (i+j)%2
    # else:
    #     res = [[0] * n for _ in range(n)]
    #     for i in range(n):
    #         for j in range(n):
    #             res[i][j] = (i+j)%2
    
    if trans == 1:
        res2 = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                res2[i][j] = res[j][i]
        res = res2
    
    # if not 'res' in locals():
    #     print(trans)
    #     print(ui)
    #     print(vi)
    #     print(cap0)
    #     print(cap1)
    #     print(cup0)
    #     print(cup1)
    
    return res

ans = [[0] * n for _ in range(n)]
for i in range(63,-1,-1):
    ui = [(j>>i)&1 for j in u]
    vi = [(j>>i)&1 for j in v]
    res = calc(ui,vi)
    for i in range(n):
        for j in range(n):
            ans[i][j] *= 2
            ans[i][j] += res[i][j]

print('\n'.join(map(lambda x: ' '.join(map(str,x)),ans)))

# for i in ans:
#     print(list(map(bin,i)))

# check
for i in range(n):
    tmp = ans[i][0]
    if s[i] == 0:
        for j in range(1,n):
            tmp &= ans[i][j]
    else:
        for j in range(1,n):
            tmp |= ans[i][j]
    if tmp != u[i]:
        print('error')
        exit()
for i in range(n):
    tmp = ans[0][i]
    if t[i] == 0:
        for j in range(1,n):
            tmp &= ans[j][i]
    else:
        for j in range(1,n):
            tmp |= ans[j][i]
    if tmp != v[i]:
        print('error')
        exit()
