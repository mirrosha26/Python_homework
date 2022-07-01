'''
Отобразить состав числа

'''

number = int(input("Введите число: "))
while number > 0:
    digit = number%10
    print("|" + str(digit), end="")
    number //= 10
else:
    print("|")
