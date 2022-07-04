''''
Обработка типовых ошибок
'''
print("Операции со писком чисел: ")
#Контролируемый код
try:
  nums = eval(input("Введите спсиок чисел: "))
  print("Получено значение: "+ str(nums))
  a = int(nums[0])
  b = int(nums[3])
  print(str(a) + "/" + str(b) + " = " + str(a/b))
except ValueError:
  print("ValueError: Ошибка при преобразовании!")
except NameError:
  print("NameError: неверный идентификатор!")
except IndexError:
  print("IndexError: неверный индекс элемента!")
except SyntaxError:
  print("SyntaxError:  невозможно вычислить выражение!")
except ZeroDivisionError:
  print("ZeroDivisionError: попытка деления на ноль!")
except TypeError:
  print("TypeError: недопустимая операция!")
