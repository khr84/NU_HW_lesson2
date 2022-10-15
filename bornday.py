bornyear = int(input('Введите год рождения А.С. Пушкина: '))
if bornyear == 1799:
    bornday = int(input('Введите день рождения А.С. Пушкина: '))
    if bornday == 6:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')