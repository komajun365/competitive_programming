def floor_sum(n, m, a, b):
    res = 0
    while True:
        if a >= m:
            res += (n - 1) * n * (a // m) // 2
            a %= m
        if b >= m:
            res += n * (b // m)
            b %= m
        y_max = (a * n + b) // m
        if y_max == 0: break
        x_max = b - y_max * m
        res += (n + x_max // a) * y_max
        n, m, a, b = y_max, a, m, x_max % a
    return res
