

def chet(a):
    if a == 1:
        res = "x>0 and y>0"
    if a == 2:
        res = "x<0 and y>0"
    if a == 3:
        res ="x<0 and y<0"
    if a == 4:
        res = "x>0 and y<0"
    return res 
a = int(input("Введите номер четверти "))
res = chet(a)
print(f"Диапазон координат в этой четверти: {res} ")
