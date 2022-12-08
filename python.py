#1
day= int(input("Введите номер дня недели: "))
if day == 6 or day == 7:
    print("Да, это выходной!")
else:
    print("Нет, это не выходной(")

#2
print("x y z")    
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x or y or z)== (not(x)) and (not(y)) and (not(z))):
                print(x,y,z)
