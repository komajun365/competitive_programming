ss = input()

ans = [0] * len(ss)

now = 'R'
last = -1
left = -1
right = -1

for i,s in enumerate(ss):
    if(s != now):
        if(s == 'L'):
            now = 'L'
            left = i-1
            right = i
        else:
            now='R'
            sumnum = i-1 - last
            if(sumnum%2 == 0):
                ans[left] = sumnum//2
                ans[right] = sumnum//2
            else:
                ans[left] = sumnum//2 + (left-last)%2
                ans[right] = sumnum//2 + (right-last)%2
            last = i-1

sumnum = i - last
if(sumnum%2 == 0):
    ans[left] = sumnum//2
    ans[right] = sumnum//2
else:
    ans[left] = sumnum//2 + (left-last)%2
    ans[right] = sumnum//2 + (right-last)%2

print(' '.join(map(str, ans)))
