'''
Инвертировать все цифры числа в их дополнения 9
'''
num = int(input("Введите число: "))
len = 0
res = 0
while num!=0:
  res += ((9-num)%10)*10**len
  len+=1
  num //= 10

print("Операция: Инвертировать все цифры числа в их дополнения 9.")
print("Результат: " + str(res))
