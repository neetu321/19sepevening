user=input("pl enter the number of rows of stars u wish")

for i in range(int(user)):
    for j in range(i+1):
        print('*',end='')
    print('\n')