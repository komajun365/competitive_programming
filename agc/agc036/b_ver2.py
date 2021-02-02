n, k = map(int, input().split())

a_list = list(map(int, input().split()))

def print_ans(s):
    if len(s)==0:
        print()
    else:
        ans = str(s[0])
        for val in s[1:]:
            ans = ans + " {}".format(val)
        print(ans)

s = []
count = 0
flag = True
done_list = [[]]
while(flag):
    count += 1
    s.extend(a_list)

    count_s = 0
    flag_in = True
    while(flag_in):
        if s[count_s] in s[count_s+:]:
            s = [s[1:].index(s[0])]







    for a in a_list:
        if a in s:
            s = s[0:s.index(a)]
        else:
            s.append(a)

    if count == k:
        print_ans(s)
        exit()

    if s in done_list:
        flag = False
    else:
        done_list.append(s.copy())


loop_num = len(done_list)
s = done_list[ k % loop_num ]
print_ans(s)
