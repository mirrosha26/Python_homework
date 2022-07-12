'''
Знакомство с кортежами
'''
# разные способы создания кортежей
Alpha = (5,10,15,"двадцать")
Bravo = 100,["один", "два", "три"], 200
Charlie = tuple([1,2,3,(4,5,6,7,8,9)])
Delta = tuple("ФИСВУА")
Echo =tuple(2**k for k in range(11))
print(Echo)

# считывание эллементов и получение срезов:
print("Alpha: ", Alpha )
print("Элементов: ", len(Alpha) )
print("Первый: ", Alpha[0] )
print("Последний: ", Alpha[-1] )
print("---------------")
print("Bravo: ", Bravo )
print("Элементов: ", len(Bravo) )
print("Bravo[1]: ", Bravo[1] )
print("Bravo[1][2]: ", Bravo[1][2] )
print("---------------")
print("Charlie: ", Charlie )
print("Элементов: ", len(Charlie) )
print("Charlie[3]: ", Charlie[3] )
print("Charlie[3][1:4]: ", Charlie[3][1:4] )
print("---------------")
print("Delta: ", Delta )
print("Элементов: ", len(Delta) )
print("Delta[-3:]: ", Delta[-3:])
print("---------------")
print("Echo: ", Echo )
Foxrot = tuple(Echo[k] for k in range(len(Echo)) if k%2 == 0)
print("Foxrot: ", Foxrot )
Golf = Echo[2:5]
print("Golf: ", Golf )
