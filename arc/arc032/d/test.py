m = [0,0]
for i in range(3001):
    tmp = (3000-i) * (3000-i) * i
    if m[1] < tmp:
        m = [i,tmp]
print(m)