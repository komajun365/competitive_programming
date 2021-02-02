s = input()

ans = 'Yes'

for i,foot in enumerate(s):
    if(i%2 == 0):
        if(foot == 'L'):
            ans ='No'
    if(i%2 == 1):
        if(foot == 'R'):
            ans ='No'

print(ans)
