t = input('please type your text : \n')

sum = 0
for i in t :
    if i.isdigit() == True :
        z = int(i)
        sum = sum + z
print(sum)            