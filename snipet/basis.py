def get_base(x,basis):
    for b in basis:
        x = min(x,x^b)
    return x

basis = []
for num in nums:
    x = get_base(num,basis)
    if x != 0:
        basis.append(x)
