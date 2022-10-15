bornyear = 0
bornday = 0
# цикл по году рождения
while bornyear != 1799:
    bornyear = input('Введите год рождения А.С. Пушкина: ')
    # проверка на ввод числа для года
    if bornyear.isdigit():
        bornyear = int(bornyear)
        # проверка года
        if bornyear == 1799:
            # цикл по дню рождения
            while bornday != 6:
                bornday = input('Введите день рождения А.С. Пушкина: ')
                # проверка на ввода числа для дня
                if bornday.isdigit():
                    bornday = int(bornday)
                    # проверка дня
                    if bornday == 6:
                        print('Верно')
                    else:
                        print('Неверный день рождения')
                else:
                    print('Неверный день рождения')
        else:
            print('Неверный год рождения')
    else:
        print('Неверный год рождения')