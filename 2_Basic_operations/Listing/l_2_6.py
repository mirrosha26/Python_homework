'''
Цикл For,
Последовательность Фибоначчи
'''

size = int(input("Введите кол-во чисел Фибоначи: "))
a,b = 1,1
for i in range(1,size+1):
    print(a, end=" ")
    a, b = b, a+b
