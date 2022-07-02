# Делители числа
num = int(input("Введите число: "))
k = 1
while k < num // 2:
    k += 1
    if num%k != 0:
        continue
    print("Делится на ", k)
print("Делится на ", num)
