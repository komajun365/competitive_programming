# a,b = map(int,input().split())
# a = list(map(int,input().split()))
# a = [list(map(int,input().split())) for _ in range(n)]

# import sys
# read = sys.stdin.buffer.read
# readline = sys.stdin.buffer.readline
# readlines = sys.stdin.buffer.readlines

# 検討?分　実装分 バグとり分

from numba import jit,prange

@jit('i8(i8)',nopython=True, parallel=True)
def calc_94(n):
    tot = 0
    for k in range(n//6 - 1):
        k -= 1
        if(k % 10**7==0):
            print(k)
        num = (3*k+1)*(k+1)
        num2 = (int(num**0.5 + 0.1))**2
        if(num == num2):
            tot += 6*k + 4

        num = k*(3*k+2)
        num2 = (int(num**0.5 + 0.1))**2
        if(num == num2):
            tot += 6*k + 2
    return tot

def main():
    n = 10**9
    print(calc_94(n))


if __name__ == '__main__':
    main()

'''
x,y(=x-1,x+1),z

x^2+(y/2)^2 =
x = 2k+1として
y = k,k+1

z^2 = 3k^2 + 4k + 1 , 3k^2 + 2k


3k^2 + 4k + 1 = (3k+1)(k+1)
3k^2 + 2k = k(3k+2)


しのごの考えずに全探索する？10**8ぐらいだし。

'''
