import sys
import os
f = open('../../input.txt', 'r')
sys.stdin = f


a,b,c = map(int, input().split())
ans = a**2 + b**2 + c**2 - 2*(a*b + b*c + a*c)
if(c-a-b < 0):
    print('No')
    exit()

if(ans > 0):
    print('Yes')
else:
    print('No')


# a,b,c = map(int, input().split())
#
# ans = c**(1/2) - b**(1/2) - a**(1/2)
# if(ans > 0):
#     print('Yes')
# else:
#     print('No')

# ans = a**2 + b**2 + c**2 - 2*(a*b + b*c + a*c)
