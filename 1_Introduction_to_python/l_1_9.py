'''
Знакомство с оператором цикла.
Вычисление суммы. Использую eval()
'''
n = input("Введите n - верхнюю границу суммы арифметической прогрессии вмда Σ=1+2+3...+n) : ")
m = 1 # переменная, принимающая значения от 1 до n в цикле
txt_sum = "1"
while str(m) != n: 
  m += 1
  txt_sum = txt_sum + "+" + str(m)
print(txt_sum + "=",eval(txt_sum))
