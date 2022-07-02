'''
Поиск простых чисел
'''
def simple(number):
    num = number//2
    k = 2 #начальное значение делителя
    while k<num:
        if number%k == 0:
            break
        k+=1
    else:
        print(number, end =" | ")
print("Поиск простого числа в списке натуральных чисел от 1 до n")
n = int(input('Введите n: '))
for i in range(n):
    simple(i)
print("Поиск заврешен")
