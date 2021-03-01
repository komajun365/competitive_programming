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
read = sys.stdin.read

t,*s = read().split()
ans = []
for si in s:
    l = len(si)
    ca = si.count('a')
    cb = l-ca
    if cb == 0:
        ans.append(si)
    elif ca % 2 == 0:
        if si[-1] == 'b':
            ans.append('b' * cb)
        else:
            cnt = si.split('b')
            tail = len(cnt[-1])
            for i in range(len(cnt)-1):
                if len(cnt[i]) > 2:
                    tail += len(cnt[i]) - 2
            if tail % 2==1:
                tail -= 1
            ans.append('b' * cb + 'a' * tail)
    else:
        if si[:ca].count('a') == ca:
            ans.append('a' + 'b' * cb)
        elif cb == 1:
            if si[0] == 'b':
                ans.append(si)
            else:
                ans.append('b' + 'a' * (ca-2))
        elif si[-1] ==  'a':
            cnt = si.split('b')
            tail = len(cnt[-1])
            for i in range(len(cnt)-1):
                if len(cnt[i]) > 2:
                    tail += len(cnt[i]) - 2
            if tail % 2==0:
                tail -= 1
            res = 'b' * cb + 'a' * tail
            ans.append(res)

        else:
            res1 = ''
            num_a = 0
            ind_a = -1
            for i in range(l):
                if si[i] == 'b':
                    res1 += 'b'
                else:
                    num_a += 1
                    if num_a == ca:
                        res1 += 'a'
                        ind_a = i

            si = si[:ind_a+1]
            cnt = si.split('b')
            move = max(len(cnt[0])-2,0)
            tail = 0
            for i in range(1,len(cnt)):
                tail = max(tail, len(cnt[i]) + move)
                if len(cnt[i]) > 2:
                    move += len(cnt[i]) - 2
            if tail % 2==0:
                tail -= 1
            res2 = 'b' * (cb-2) + 'a' * tail
            if res1 > res2:
                ans.append(res1)
            else:
                ans.append(res2)


print('\n'.join(ans))
