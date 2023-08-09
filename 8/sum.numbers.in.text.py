t = input('please type your text : \n')

sum = 0
for i in t :
    if i.numeric() == True :
        z = int(i)
        sum = sum + z
print(sum)            