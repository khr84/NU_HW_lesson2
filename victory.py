# 1 Галилео Галилей - 1564
# 2 Исаак Ньютон - 1642
# 3 Чарльз Дарвин - 1809
# 4 Томас Эдисон - 1847
# 5 Альберт Эйнтштейн - 1879
repeat_game = True
# цикл по игре (в зависимости от ответа игрока)
while repeat_game:
    itteration = 0
    count_true = 0
    # цикл по персонам и расчет кол-ва правильных ответов
    while itteration < 5:
        if itteration == 0:
            person = 'Галилео Галилей: '
            person_year = 1564
        elif itteration == 1:
            person = 'Исаак Ньютон: '
            person_year = 1642
        elif itteration == 2:
            person = 'Чарльз Дарвин: '
            person_year = 1809
        elif itteration == 3:
            person = 'Томас Эдисон: '
            person_year = 1847
        elif itteration == 4:
            person = 'Альберт Эйнтштейн: '
            person_year = 1879
        itteration += 1

        bornyear = ''
        # ждем числовое значение
        while not bornyear.isdigit():
            bornyear = input('Введите год рождения ' + person)
        if int(bornyear) == person_year:
            count_true += 1

    print('Количество правильных ответов:', count_true)
    print('Количество ошибок:', 5 - count_true)
    print('Процент правильных ответов:', count_true * 100 / 5)
    print('Процент ошибок:', 100 - count_true * 100 / 5)
    repeat_str = ''
    # ждем числовой ответ от игрока
    while not repeat_str.isdigit():
        repeat_str = input('Хотите сыграть еще раз? 1 - Да, 0 - Нет: ')
    # ждем корректные 1/0
    while int(repeat_str) != 1 and int(repeat_str) != 0:
        repeat_str = input('Хотите сыграть еще раз? 1 - Да, 0 - Нет: ')
    if int(repeat_str) == 1:
        repeat_game = True
        print('\n Сыграем еще раз')
    elif int(repeat_str) == 0:
        repeat_game = False
        print('Спасибо за игру')