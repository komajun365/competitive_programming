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
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n,q,*data = map(int,read().split())
h = data[:n]
query = data[n:]

dif = []
cnt = dict()
for i in range(n-1):
    if(i%2==0):
        di = h[i+1] - h[i]
    else:
        di = h[i] - h[i+1]
    dif.append(di)
    if(di in cnt):
        cnt[di] += 1
    else:
        cnt[di] = 1

base = 0
ans = []
idx = 0
for _ in range(q):
    if(query[idx] == 3):
        ui,vi = query[idx+1:idx+3]
        idx += 3
        ui -= 1
        if(ui != 0):
            bef = dif[ui-1]
            if(ui % 2 == 0):
                aft = bef - vi
            else:
                aft = bef + vi
            cnt[bef] -= 1
            if(aft in cnt):
                cnt[aft] += 1
            else:
                cnt[aft] = 1
            dif[ui-1] = aft
        if(ui != n-1):
            bef = dif[ui]
            if(ui % 2 == 0):
                aft = bef - vi
            else:
                aft = bef + vi
            cnt[bef] -= 1
            if(aft in cnt):
                cnt[aft] += 1
            else:
                cnt[aft] = 1
            dif[ui] = aft

    else:
        vi = query[idx+1]
        if(query[idx] == 1):
            base += vi
        else:
            base -= vi
        idx += 2
        
    if(base in cnt):
        ans.append(cnt[base])
    else:
        ans.append(0)
    # print(base)
    # print(cnt)

print('\n'.join(map(str,ans)))