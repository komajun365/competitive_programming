import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

# import sys
# input = sys.stdin.readline

n = int(input())
s = input()
q = int(input())

#seg_tree
def init(n, s):
    num = len(str(bin(n-1))) -2
    seg = [0] * (2**(num+1))
    seg_num = 2**num

    for i in range(n):
        tmp = ord(s[i]) - 97
        seg[i + seg_num] = 1 << tmp

    for i in range(seg_num-1, 0, -1):
        seg[i] = seg[i*2] | seg[i*2+1]

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
        ans = ans | seg[i]
    ans = str(bin(ans)).count('1')
    return(ans)

def update(i,s):
    i += seg_num
    tmp = ord(s) - 97
    seg[i] = 1 << tmp
    while(i > 1):
        i = i//2
        seg[i] = seg[2*i] | seg[2*i+1]

seg,seg_num = init(n,s)

for i in range(q):
    q1,q2,q3 = input().split()
    if(q1 =='1'):
        update(int(q2)-1, q3)
    else:
        q2,q3 = int(q2),int(q3)
        print(calc_sum(q2-1, q3-1))
