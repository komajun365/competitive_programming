n,y = map(int,input().split())

n_10 = -1
n_5 = -1
n_1 = -1

y_temp = y / 1000
y_temp = y_temp - n

n_10 = y_temp//9

count = 0
while(count < 4):
    remine = y_temp - n_10*9
    if(remine % 4 == 0 ):
        n_5 = remine/4
        n_1 = n - n_10 - n_5
        if (n_10 < 0) | (n_5 < 0) | (n_1 < 0):
            n_10 = -1
            n_5 = -1
            n_1 = -1
        count = 10
    else:
        n_10 -= 1
        count += 1
        if count == 4:
            n_10 = -1
            n_5 = -1
            n_1 = -1

print("{} {} {}".format(int(n_10),int(n_5),int(n_1)))
