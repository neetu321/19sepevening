print("first file printed")

l1=[12,32,43,54]
l2=[]
for element in l1:
    if element%2==0:
        l2.append(element)
print(l2,"is a list of even numbers")