'''
Создание списков и операции с ними
'''
# Список из чисел
nums = [1,2,3,12,45,-18]
#отображение содержимого списка 
print("Список из чисел:", nums)
#Длина списка 
print("Длина списка:", len(nums))
#Первый элемент списка
print("Первый элемент", nums[0])
#Последний элемент списка
print("Последний элемент", nums[-1])
#Наибольшее значение
print("Наибольшее значение:", max(nums))
#Наименьшее значение
print("Наименьшее значение:", min(nums))
#Сумма
print("Сумма:", sum(nums))
#Список в обратном порядке 
print("Список в обратном порядке: ", list(reversed(nums)))
#Сортировка по возрастанию значений
print("По возрастанию значений: ", sorted(nums))
#Сортировка по убыванию значений
print("По убыванию значений: ", sorted(nums, reverse = True))
#Исходнй список 
print("Исходный список: ", nums)
#Изменение значения элемента списка 
nums[1] = "Миша"
#Отображение содержимого списка 
print("После внесения изменений: ", nums)
#Получение среза
print("Получение среза: ", nums[1:-1])
#Замена части элементов списка 
nums[1:-1] = ["A", "B"]
#После замены элементов:
print("После замены элементов: ", nums)
#Список чисел от 5 до 10
nums = list(range(5, 11))
print("Список чисел от 5 до 10 : ", nums)
#Удаление элементов из списка: 
nums[2:4] = []
print("После удаления двух элементов : ", nums)
#Удаление последнего элемента
del nums[-1]
print("Удален последний элемент: ", nums)
#Нечетные числа
nums = [ 2*k+1 for k in range(5)]
print("Нечетные числа: ", nums)
#Список символов создается на освнове текста 
symbs = list("Python")
#Отображение содержимого списка
print("Список символов: ", symbs)
#Два первых символа
print("Два первых символа: ", symbs[:2])
#Остальные списки 
print("Остальные символы: ", symbs[2:])
