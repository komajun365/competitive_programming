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

# l = int(input())
mod = 1000000007

def calc1():
    al = (l-1)//4 + 1
    ar = (l-3)//3
    if al > ar:
        return 0

    xl = l - 3*al - 2
    xr = l - 3*ar - 2
    res = (xl+xr) * (ar-al+1) //2
    return res

def calc2():
    al = 2
    ar = (l-1)//4
    if al > ar:
        return 0

    xl = al-1
    xr = ar-1
    res = (xl+xr) * (ar-al+1) //2
    return res

def calc3():
    bl = l//3 + 1
    br = (l-3)//2
    if bl > br:
        return 0

    xl = l - bl*2 - 2
    xr = l - br*2 - 2
    res = (xl+xr) * (br-bl+1) //2
    return res

def calc4():
    bl = 3
    br = l//3
    if bl > br:
        return 0

    xl = bl-2
    xr = br-2
    res = (xl+xr) * (br-bl+1) //2
    return res

def calc5():
    bl = 3
    br = l//3
    return max(0, br-bl+1)

def solve(l):
    ans = calc1() + calc2() + calc3() + calc4() - calc5()
    ans %= mod
    return ans

def solve_simple(l):
    res = 0
    for a in range(2,l+1):
        if a*3 > l:
            break
        for b in range(a+1,l+1):
            if a+2*b > l:
                break
            for c in range(b+1,l+1):
                if a+b+c > l:
                    break
                if c >= a+b:
                    break
                if a+1 == b or b+1 == c:
                    res += 1
                    # print('ex:',a,b,c)
    return res

n = 5
for l in range(n,n+100):
    res1 = solve(l)
    res2 = solve_simple(l)
    if res1 != res2:
        print(l,res1,res2)

# solve_simple(9)



# print(calc1())
# print(calc2())
# print(calc3())
# print(calc4())
# print(calc5())


'''
a<b<c として

・a+1==bのとき
b+1 <= c < min(l-(a+b)+1,a+b)

・b+1==cのとき
2 <= a < min(b, l-(b+c)+1)

'''