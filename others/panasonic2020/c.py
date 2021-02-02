import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f

a,b,c = map(int, input().split())
mod = 10**5

def calc(x,y):
    x0 = x % mod
    x1 = x // mod
    y0 = y % mod
    y1 = y // mod
    ans0 = x0*y0 % mod
    ans1 = (x0*y0 // mod) + (x1*y0 % mod) + (x0*y1 % mod)
    ans2 = x1*y1 + ans1//mod
    ans1 = ans1 % mod
    return([ans2,ans1,ans0])

a_2 = calc(a,a)
b_2 = calc(b,b)
c_2 = calc(c,c)
ab = calc(2*a,b)
ac = calc(2*a,c)
bc = calc(2*b,c)

def calc2(x,y,z):
    ans = [0,0,0]
    for i in range(3):
        ans[i] = x[i] + y[i] + z[i]

    ans[1] += ans[2] // mod
    ans[0] += ans[1] // mod
    ans[1] = ans[1] % mod
    ans[2] = ans[2] % mod

    return(ans)

plus = calc2(a_2,b_2,c_2)
minus = calc2(ab, ac, bc)

for i in range(3):
    if(plus[i] > minus[i]):
        print('Yes')
        exit()
    elif(plus[i] < minus[i]):
        print('No')
        exit()


print('No')
# if(ans > 0):
#     print('Yes')
# else:
#     print('No')


# a,b,c = map(int, input().split())
#
# ans = c**(1/2) - b**(1/2) - a**(1/2)
# if(ans > 0):
#     print('Yes')
# else:
#     print('No')

# ans = a**2 + b**2 + c**2 - 2*(a*b + b*c + a*c)
