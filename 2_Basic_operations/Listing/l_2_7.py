'''
## Поиск букв в тексте до первого совпадения
Использование конструкции
    for переменная in список:
        #команды
    else:
        #команды
'''
mytext = input("Введите текст для проверки: ")
symbs = ['а','у','я']
print("Ищем такие буквы: ", symbs)
for s in symbs:
    if s in mytext:
        print("В тексте есть буква '" + s +"'")
        break
    else:
        print("В тексте нет буквы '" + s +"'")
else:
    print("Таких букв в тексте нет")
print("Поиск завершен")
