'''
Напишите программу, в которой расстояние, указанное в милях,
переводится в километры. Учесть, что одна миля примерно равна
1,6 километра. Расстояние в милях вводится пользователем с клавиатуры.
'''
mi = float(input("Введите расстояние в милях: "))
km = round(mi*1.60934,1)
print("Ваше расстояние в километрах: ", km, "км")
