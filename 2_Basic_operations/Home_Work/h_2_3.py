'''
Собрать объединением из списка целых чисел одно целое число
'''
print("Операция: Собрать объединением из списка целых чисел одно целое число.")
nums = eval(input("Введите список целых чиcел: "))
snum =""
for i in nums:
  snum += str(i)
num = int(snum)
print("Результат: ",num )
