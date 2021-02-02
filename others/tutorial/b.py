inp = []
for i in range(3):
    inp.append(input())

num = 0
# num = inp[0]
for i in range(2):
    num += sum(list(map(int, inp[i].split())))
# num += sum(list(map(int, inp[2].split())))

print("{} ".format(num) + inp[2])
