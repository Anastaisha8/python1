def inputK(x):
    a = [0]*x 
    for i in range(x):
        is_True = False 
        while not is_True:
            try:
                number = float(input(f"Введите {i+1} координату: "))
                a[i] = number 
                is_True = True
                if a[i] == 0:
                    is_True = False 
                    print("Координата не может равняться 0")
            except ValueError:
                print("Ошибка!!! Необходимо ввести числа ")
    return a

def coord(xy):
    text = 4 
    if xy[0]<0 and xy[1]>0:
        text = 2
    elif xy[0]>0 and xy[1]>0:
        text = 1
    elif xy[0]< 0 and xy[1]<0:
        text = 3 
    print (f"Точка находится в {text} четверти плоскости")
koord = inputK(2)
coord(koord)