'''
Знакомство с оператором цикла.
Вычисление суммы, нормальные способы
'''
n = int(input("Введите n - верхнюю границу суммы арифметической прогрессии вмда Σ=1+2+3...+n) : "))
#Через список
print("Сумма целых чисел от 1 до ", n, " равна", sum(list(range(1,n+1)))) 
#По формуле 
print("Сумма целых чисел от 1 до ", n, " равна", int(n*(n+1)/2)) 