'''
Решение линейного уравнения
A*X = B
'''
a,b = eval(input("Введите (через запятую) два числа: "))
if (type(a)==int or tybe(a)==float) and (type(b)==int or tybe(b)==float):
    print("Уравнение "+str(a)+"*x = "+str(b))
    if a!=0:
        print("Ответ: х = " + str(b/a))
    else:
        if b!=0:
            print("Ответ: Решений нет")
        else:
            print("Ответ: любое число")
else:
    print("Введены некорректные значения!")
    raise SystemExit(0)
print("Поиск решения завершен.")
