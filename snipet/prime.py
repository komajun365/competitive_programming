# 素数系の関数を作っておく

# 素因数分解
# n=1の時に素因数1を出力しちゃうやつ
# def factorization(n):
#     arr = []
#     temp = n
#     for i in range(2, int(n**0.5//1)+1 ):
#         if(temp%i == 0):
#             count=0
#             while( temp%i == 0):
#                 count += 1
#                 temp = temp // i
#             arr.append([i, count])
#     if(temp != 1):
#         arr.append([temp, 1])
#     if(arr == []):
#         arr.append([n, 1])
#     return arr

# 素因数分解
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(n**0.5//1)+1 ):
        if(temp%i == 0):
            count=0
            while( temp%i == 0):
                count += 1
                temp = temp // i
            arr.append([i, count])
        if temp==1:
            break

    if(temp != 1):
        arr.append([temp, 1])
    
    return arr


# 約数のリストを作る
# sortはされてないのできをつけよう
def make_divisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if(n%i == 0):
            divisors.append(i)
            if(i!= n//i):
                divisors.append(n//i)

    return  divisors

#エラストテネスの篩
#n以下の素数のリストを返却
#2n+1だけ見る : 10**7 でpython3:1400ms, pypy3:700msくらい
def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    primes_append = primes.append
    len_list = (n+1)//2
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_list):
        if(flags[i]):
            primes_append(i*2+1)
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return primes

#エラストテネスの篩
#n以下の素数のリストを返却
#2n+1だけ見る : 10**7 でpython3:900ms, pypy3:700msくらい
def sieve(n):
    if( n <= 1):
        return []
    elif(n==2):
        return [2]

    primes = [2]
    len_list = (n+1)//2
    len_sqrt = int(len_list**0.5) + 1
    flags = [True] * len_list
    flags[0] = False
    for i in range(len_sqrt):
        if(flags[i]):
            start = ((i*2+1)**2)//2
            for j in range( start, len_list, i*2+1):
                flags[j] = False
    return [2] + [i*2+1 for i in range(len_list) if flags[i]]



# 6n+1,6n+5を見ようとして断念
# def sieve(n):
#     if( n <= 6):
#         primes = [2,3,5]
#         ret = []
#         for i in primes:
#             if(i<=n):
#                 ret.append(i)
#         return ret
#     len_list = (n//6 * 2 + (n%6 >= 1) + (n%6 >= 5) )
#     flags = [True] * len_list
#     flags[0] = False
#     for i in range(len_list):
#         if(flags[i]):
#             num = (i//2) * 6 + 1 + (i%2)*4


# left　<=　p　<　right な素数のリスト
# right-left が10**7くらいまで、　かつ、　rightが10**14くらいまでのとき使える
def sieve_range(left,right):
    n = 100 + int(right**0.5)
    primes_base = sieve(n)

    if( len(primes_base)==0):
        return []

    primes = []
    left += (left%2 == 0)
    len_list = (right-left)//2 + 1
    flags = [True] * len_list
    for i in primes_base[1:]:
        dif = (i - (left % i))%i
        if(dif%2 == 1):
            dif += i
        start = dif//2
        for j in range( start, len_list, i):
            flags[j] = False
    return [i*2+left for i in range(len_list) if flags[i]]
