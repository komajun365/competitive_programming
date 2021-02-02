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

q,*data = read().split()
q = int(q)
dq = []
ind = 0

ans = []
i = 0
for _ in range(q):
    if(data[i] == '1'):
        ci = ord(data[i+1]) - ord('a')
        xi = int(data[i+2])
        dq.append([ci,xi])
        i += 3
    else:
        di = int(data[i+1]) 
        cnt = [0] * 26
        while(ind < len(dq)):
            if(dq[ind][1] > di):
                dq[ind][1] -= di
                cnt[dq[ind][0]] += di
                break
            cnt[dq[ind][0]] += dq[ind][1]
            di -= dq[ind][1]
            dq[ind][1] = 0
            ind += 1
        tmp = 0
        for cni in cnt:
            tmp += cni**2
        ans.append(tmp)
        i += 2

print('\n'.join(map(str,ans)))

