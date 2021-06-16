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

l = int(input())
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

ans = calc1() + calc2() + calc3() + calc4() - calc5()
ans %= mod
print(ans)

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