n = int(input())

# alp = ["a","b","c","d","e",
# "f","g","h","i","j",
# "k","l","m","n","o",
# "p","q","r","s","t",
# "u","v","w","x","y","z"]
#
ans = 0
# array1 = np.zeros().reshape( n,10)


# list1 = []
list_s = []

for i in range(n):
    s = input()
    list_s.append(s)

list_s = list(map(sorted, list_s))



ans = sum(map(lambda y: (sum(map(lambda x: x==list_s[y],list_s)) -1),list(range(n))))
# for i in range(n):
#     ans = ans + sum(map(lambda x: x==list_s[i],list_s)) -1

print(int(ans/2))
