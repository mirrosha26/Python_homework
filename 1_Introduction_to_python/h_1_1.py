'''Напишите программу, которая в которой программа запрашивает у пользователя день и месяц,
а затем выводит сообщение о текущем дне и месяце'''

month = input("Введите текщий месяц: ").lower()
# меняю падеж с месяца с им-го на род-й 
dictMonth = {"январь":"января","февраль":"февраля", "март":"марта", "апрель":"апреля", "май":"мая", "июнь":"июня", "июль":"июля", "август":"августа", "сентябрь":"сентября", "октябрь":"октября", "ноябрь":"ноября", "декабрь":"декабря"}
day = input("Введите текущий день: ")
print("Сегодня", day, dictMonth[month])
