'''
сравнить два числа, обработать ошибки
'''
try:
  a,b = eval(input("Введите два действительных числа через запятую: "))
  res = str(a) + " > " + str(b)  if a > b else str(a) + " < " + str(b)
  print(res)

except TypeError:
  print("Ошибка ввода! (TypeError. Недопустимая операция!)")
except NameError:
  print("Ошибка ввода! (NameError. неверный идентификатор!)")
except NameError:
  print("Ошибка ввода! (NameError. неверный идентификатор!)")
except:
  print("Ошибка ввода!")
