n = int(input())

ans = 0
ans_dict = {}

for i in range(n):
    s = input()
    s = ''.join(sorted(s))
    if(s in ans_dict):
        ans += ans_dict[s]
        ans_dict[s] += 1
    else:
        ans_dict[s] = 1
        
print(int(ans))
