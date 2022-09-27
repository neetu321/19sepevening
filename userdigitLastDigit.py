user=input("type a number")
print(user[-1])

a='neetu'
b='aeiou'
c=''
for element in a:
    if element not in b:
        c=c+element
print(c)