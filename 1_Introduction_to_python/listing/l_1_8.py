'''
Знакомство с оператором цикла.
Вычисление суммы. Σ=1+2+3...+n
'''
n = int(input("Введите n - верхнюю границу суммы арифметической прогрессии вмда Σ=1+2+3...+n) : "))
sum = 0 
m = 0 # переменная, принимающая значения от 1 до n в цикле
while m < n: 
  m +=1
  sum = sum + m 
print("Сумма чисел от 1 до", n, "равна", sum)
