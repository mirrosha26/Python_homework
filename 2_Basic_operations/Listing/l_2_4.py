#Делители числа
num = int(input("Введите число: "))
k = 1
while k <= num//2:
    if num%k == 0:
        print("Делится на", k)
    k += 1
print("Делится на", num)
