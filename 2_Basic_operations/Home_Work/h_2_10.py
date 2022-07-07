'''
Решить уравнение:
Ax = B - A - 1
'''
print("Ax = B - A - 1")
try:
    a, b = eval(input("Введите A, B через запятую: "))
    if a!=0:
        x = ( b - 1)/a - 1
    elif b == 1:
        x = "любое число"
    else:
        x = "решений нет"
    print("Ответ:",x)
except:
    print("Ошибка ввода!")
