'''
Является ли число простым?
'''
number = int(input('Введите число: '))
k = 2 # Начальный делитель
num = number//2
while k<num:
    if number%k == 0:
        print("Число не является простым")
        break
    k+=1
else:
    print("Это простое число")
print("Проверка заврешина")
