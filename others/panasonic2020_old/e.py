import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a = input()
b = input()
c = input()

def calc(a,b):
    ans = ''
    for i in range(len(a)):
        len_ab = min(len(a)-i, len(b))
        tmp_a = a[i: i+len_ab]
        tmp_b = b[:len_ab]
        tmp = ''
        flag = 1
        for j in range(len_ab):
            if(tmp_a[j]==tmp_b[j]):
                tmp += tmp_a[j]
            elif(tmp_a[j]=='?'):
                tmp += tmp_b[j]
            elif(tmp_b[j]=='?'):
                tmp += tmp_a[j]
            else:
                flag = 0
                break
        if(flag == 1):
            ans = ans + tmp + a[i+len_ab:] + b[len_ab:]
            return(ans)
        else:
            ans += a[i]
    return(a+b)

ans = [0]*12
ans[0] = calc(calc(a,b),c)
ans[1] = calc(calc(a,c),b)
ans[2] = calc(calc(b,a),c)
ans[3] = calc(calc(b,c),a)
ans[4] = calc(calc(c,a),b)
ans[5] = calc(calc(c,b),a)
ans[6] = calc(a,calc(b,c))
ans[7] = calc(a,calc(c,b))
ans[8] = calc(b,calc(a,c))
ans[9] = calc(b,calc(c,a))
ans[10] = calc(c,calc(a,b))
ans[11] = calc(c,calc(b,a))

ans_n = len(ans[0])
for i in range(1,12):
    ans_n = min(ans_n, len(ans[i]))


print(ans_n)
