'''
Значения разных типов через тернарный оператор
'''
val = eval(input("Введите выражение: "))
a, b = (val[0], val[-1]) if type(val) == str else (val, type(val))
print(a)
print(b) 
