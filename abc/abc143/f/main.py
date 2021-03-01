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

cnt = [0] * (n+1)
for ai in a:
    cnt[ai] += 1

nums = []
for ci in cnt:
    if ci != 0:
        nums.append(ci)

nums.sort()
l = len(nums)
max_num = nums[-1]
cnt = [0] * (max_num+1)
for ni in nums:
    cnt[ni] += 1

cumsum = [0] * (max_num+1)
for i in range(1,max_num+1):
    cumsum[i] = cumsum[i-1] + cnt[i]*i

cnt_r = [0] * (max_num+2)
for i in range(max_num,-1,-1):
    cnt_r[i] = cnt_r[i+1] + cnt[i]

# print(cumsum)
# print(cnt_r)

def calc(k,y):
    under = cumsum[min(y-1, max_num)]
    x = k - cnt_r[min(y, max_num+1)]
    if x <= 0:
        return True
    if x*y <= under:
        return True
    return False

ans = []
for k in range(1,n+1):
    if k > l:
        ans.append(0)
    else:
        ok = 0
        ng = n+1
        while( ng-ok > 1):
            mid = (ng+ok) // 2
            if calc(k,mid):
                ok = mid
            else:
                ng = mid
        ans.append(ok)

print('\n'.join(map(str,ans)))
