s='betty bought some butter. the butter was bitter'
'''
l1=s.split(" ")
print(l1)

for index in range(len(l1)):
    if l1[index]=='butter':
        print(index)
'''
inb=s.rindex('bu')
subs='butter'
print(inb)
print(inb+len(subs))








