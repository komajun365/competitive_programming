#!/usr/bin/env python

import random

MAX = 1000000000

def Generate(i, prefix, lmin, lmax, nmin, nmax, mmin, mmax):
    filename = f'{prefix}{i:02}.in'
    n = random.randint(nmin, nmax)
    m = random.randint(mmin, mmax)
    with open(filename, 'w') as f:
        f.write('{} {}\n'.format(n, m))
        ls = [random.randint(lmin, lmax) for i in range(n)]
        f.write('{}\n'.format((' '.join(map(str,ls)))))

def main():
    added = 0
    for i in range(3+added):
        Generate(i, '12-middle', 1, 10000, 900, 1000, 1, 10)
        Generate(i, '12-large', MAX-10000, MAX, 900, 1000, 1, 10)
        Generate(i, '12-all', 1, MAX, 900, 1000, 1,10)
    for i in range(2+added):
        Generate(i, '01-simple', 1, 200, 130, 140, 0, 0)
        Generate(i, '11-simple2', 1, MAX, 900, 1000, 0, 0)
        Generate(i, '02-smallsmall', 1, 100, 10, 20, 1, 10)
        Generate(i, '02-small', 1, 100, 130, 140, 0, 10)
        Generate(i, '02-random', 1, MAX, 130, 140, 0, 3)
        Generate(i, '02-large', MAX-1000, MAX, 130, 140, 0, 3)
        Generate(i, '12-small', 1, 100, 900, 1000, 0, 10)

if __name__ == '__main__':
    main()
