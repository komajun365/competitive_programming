import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

n = int(input())
p = list(map(int,input().split()))

import bisect

a = list(range(1,n*20000+1,20000))
b = a[::-1]

#seg_tree
def init(n, init_num=0):
    num = len(str(bin(n-1))) -2
    seg = [init_num] * (2**(num+1))
    seg_num = 2**num
    return seg, seg_num

def calc_sum(head, tail):
    head += seg_num
    tail += seg_num
    l = []
    while(head <= tail):
        if(head == tail):
            l.append(head)
            break

        if(head % 2 == 1):
            l.append(head)
            head += 1
        head = head //2

        if(tail % 2 == 0):
            l.append(tail)
            tail -= 1
        tail = tail //2

    ans = 0
    for i in l:
        ans += seg[i]
    return(ans)

def update(i,x):
    i += seg_num
    seg[i] = x
    while(i > 1):
        i = i//2
        seg[i] = seg[2*i] + seg[2*i+1]

seg,seg_num = init(n)

for i in p:
    i -= 1
    a[i] += calc_sum(0,i-1)
    b[i] += calc_sum(i+1,n-1)
    update(i,1)

print(' '.join(map(str, a)))
print(' '.join(map(str, b)))
