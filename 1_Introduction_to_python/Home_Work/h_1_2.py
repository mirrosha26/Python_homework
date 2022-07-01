'''
Напишите программу, в которой пользователь должен ввести текущий год и год своего рождения. 
Программа вычисляет возраст пользователя и выводит соответствующее сообщение. 
'''

year = int(input("Введите текущий год: "))
yearOfBirth = int(input("Введите год своего рождения: "))
age = year - yearOfBirth


# Формируем правильный подбор последнего слова в выводе
yearEnding = age%10
if yearEnding == 1:
    yearEndingWord = "год"
else:
    if yearEnding in {2,3,4}:
        yearEndingWord = "года"
    else:
        yearEndingWord = "лет"

print("Ваш возраст:",age,yearEndingWord )
