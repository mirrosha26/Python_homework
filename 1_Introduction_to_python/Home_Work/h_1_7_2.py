'''
Расчет факториала
'''
from functools import reduce

#Функция для запроса n, выдает необходимый спсиок членов арифметичской прогресии  
def zapros():
    n = int(input("Введите n для расчета n!: "))
    while (n < 0):
        print("Вы ввели отрицательное число!!!")
        n = int(input("Введите n для расчета n!: "))
    if n == 0:
        return [0]
    else:
        return [ i for i in range(1,n+1)]

# Расчет факториала
fact = reduce(lambda a, x: a*x, zapros() )
print(fact)
