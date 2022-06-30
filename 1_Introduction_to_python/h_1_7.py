'''
Создать программу, в которой вычисляется факториал числа n!
'''

print("Программа расчета факториала n!")
num = -1
fact = 1
while num <0 :
    num = int(input("Введите число, факториал которого нужно найти: "))
    if num < 0:
        print("Вы ввели отрицательное число!")
if num == 0:
    print(num,"! = 0")
else:
    for i in range(1,num+1):
        fact *= i
    print(num,"! =",fact)
