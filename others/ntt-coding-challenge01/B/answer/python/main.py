import numpy as np


def move_left(row):
    C = len(row)
    non_zeros = [xi for xi in row if xi != 0]
    row.fill(0)
    for i, xi in enumerate(non_zeros):
        row[i] = xi

    for i in range(C - 1):
        if row[i] == row[i+1] and row[i] != 0:
            row[i] *= 2
            row[i+1:C-1] = row[i+2:]
            row[C-1] = 0
    return row


def move(X, command):
    if command in ('U', 'D'):
        virtual_command = 'R' if command == 'D' else 'L'
        R = M
        X = X.T
    else:
        virtual_command = command
        R = N

    for k in range(R):
        if virtual_command == 'R':
            X[k] = X[k][::-1]

        X[k] = move_left(X[k])

        if virtual_command == 'R':
            X[k] = X[k][::-1]

    if command in ('U', 'D'):
        X = X.T

    return X


N, M = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))
X = np.asarray(X)
s = input()

for si in s:
    X = move(X, si)

for xi in X:
    print(' '.join(map(str, xi)))
