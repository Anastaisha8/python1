def chetv(x,y):
    if (x>0)and(y>0):
        res= 1
    if (x<0)and(y>0):
        res= 2
    if (x<0)and(y<0):
        res = 2
    if (x>0)and(y<0):
        res = 4
    
    return res
x = int(input("Введите первую координату:"))
y = int(input("Введите вторую координату:"))
res = chetv(x,y)
print(f"Точка находится в {res} четверти плоскости")