s = '''puvxlhwva
fubxha
tbxvtralb
jnerjnerun
xvzvgnpuvgb
lhxban
xnaxrvjb
xvmhxhgnzr
xbabubfuvav
lnggrxvgn
fnffbxhqntn
lhxbab
fuvehfuvgbfvgr
chermragbjb
bartnvfuvgnv
ranwvqbevaxh
mbar
jb
whaovfuvgr
ubfuvvabqn
xbabartnvjb
xnanrgrxhereron
bgbanfuvxh
xbabubfuvjb
ngbavfhehgfhzbevqn
jnerjnerun
nenfbvtbgbjb
abmbznanv
znrzhxvan
urawvjb
xvgnvfuvgrveh
'''

s = s.split()

ans = []
for si in s:
    tmp = ''
    for j in si:
        tmp += chr((ord(j) - ord('a') + 13) % 26 + ord('a'))
    ans.append(tmp)

# print(ans)
print('\n'.join(ans))