a,b = map(int, input().split())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

hoge_a = set(prime_factorize(a))
hoge_b = set(prime_factorize(b))
ans = len(hoge_a & hoge_b) +1
print(ans)
