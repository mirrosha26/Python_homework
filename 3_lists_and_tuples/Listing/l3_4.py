'''
Создание выборки
'''
# кортеж чисел:
A = tuple(k for k in range(1,21) if k%3!=0)
print(A)

# список чисел
B = [2**(k//2) if k%2==0 else 3**(k//2) for k in range(15)]
print(B)

# список чисел
C = [0 if k == 0 or k==1 else k**2 for k in range(13) if not k in [2,5,7]]
print(C)

# Кортеж в обратном порядке:
Alpha = A[::-1]
print(Alpha)

# Элементы выбирабтся "через один", начиная с первого (B)
Bravo = B[::2]
print(Bravo)

# Элементы выбирабтся "через один", начиная со второго (B)
Charlie = B[1::2]
print(B)
