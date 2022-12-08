def coord(x,y,x1,y1):
    vekt1 = x1-x 
    vekt2 = y1-y
    res = (vekt1**2+vekt2**2)**0.5
    return res 
x = int(input("Ввведите первую координату 1 точки:"))
y = int(input("Введите вторую координату 1 точки:"))
x1 = int(input("Введите первую координату 2 точки:"))
y1 = int(input("Введите вторую координату 2 точки:"))
res = coord(x,y,x1,y1)
print(f"Расстояние между данными точками: {res}")