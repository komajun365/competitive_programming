import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n,k = map(int, input().split())
pw = []
for i in range(n):
    w,p = map(int, input().split())
    pw.append([p,w])

pw.sort()
ans = pw[-1]
remain = set(range(n-1))

for i in range(1,k):
    next_i = 0
    next_p = 0
    ans_p, ans_w = ans
    for j in remain:
        tmp_p, tmp_w = pw[j]
        tmp_next_p = (ans_p*ans_w + tmp_p*tmp_w) / (ans_w+tmp_w)
        if(next_p <= tmp_next_p):
            next_i = j
            next_p = tmp_next_p

    remain.remove(next_i)
    tmp_p, tmp_w = pw[next_i]
    ans = [  (ans_p*ans_w + tmp_p*tmp_w) / (ans_w+tmp_w)
            , ans_w  +  tmp_w]

print(ans[0])
