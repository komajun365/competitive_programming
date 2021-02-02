#import numpy as np

n = int(input())
a_s = list(map(int, input().split()))

n = 3
a_s =[1,0,0]

m = 0
ans = [0]*(n+1)
#ans = np.zeros(n+1).astype(int)


i=1
for i in range(n,0,-1):
    sum_num = 0
    for j in range(i,n+1,i):
        sum_num += ans[j]

    if((sum_num & 1) != a_s[i-1]):
        m += 1
        ans[i] = 1

ans2 = []
for i in range(1,n+1):
    if ans[i]==1:
        ans2.append(i)

print(m)
print(' '.join(map(str,ans2)))
