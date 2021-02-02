import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n, d, a  = map(int,input().split())
x_b = []
x_b2 = []
x = [0]*n
h_b = []
h = [0]*n
for i in range(n):
    x_temp,h_temp = map(int,input().split())
    x_b.append({'key':i, 'val':x_temp})
    x_b2.append(x_temp)
    h_b.append(h_temp)

x_b.sort(key = lambda x_b : x_b['val'])

for i in range(n):
    ind = x_b[i]['key']
    x[i] = x_b2[ind]
    h[i] = h_b[ind]

ans = 0
for i in range(n):
    if (h[i] <= 0):
        continue
    at_num = ((h[i] -1 )// a) + 1
    ans += at_num
    h[i] -= at_num * a
    x_origin = x[i]
    while(True):
        i += 1
        if(i >= n):
            break
        if(x_origin + 2*d >= x[i]):
            h[i] -= at_num * a
        else:
            break

print(ans)
