'''
# Еще один способ решить уравнение A*X = B
Знакомлюсь с конструкцией elif:
if условие:
    # команды
elif условие:
    # команды
elif условие:
    # команды
...
elif условие:
    # команды
else:
    # команды
'''

a,b = eval(input("Введите (через запятую) два числа: "))
if (type(a)==int or tybe(a)==float) and (type(b)==int or tybe(b)==float):
    print("Уравнение "+str(a)+"*x = "+str(b))
else:
    print("Введены некорректные значения!")
    raise SystemExit(0)

if a!=0:
    print("Ответ: х = " + str(b/a))
elif b!=0:
    print("Ответ: Решений нет")
else:
    print("Ответ: любое число")
print("Поиск решения завершен.")
