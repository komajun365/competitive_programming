n = int(input())

b_list = {}
min_list = {}
max_list = {}

min_list[1], max_list[1] = 0,0

for i in range(2,n+1):
    b_list[i] = int(input())
    min_list[i], max_list[i] = 0,0

for i in range(n,1,-1):
    b = b_list[i]
    salary = 1 + min_list[i] + max_list[i]
    max_list[b] = max(max_list[b], salary)
    if min_list[b] == 0:
        min_list[b] = salary
    else:
        min_list[b] = min(min_list[b], salary)

salary = 1 + min_list[1] + max_list[1]
print(salary)
