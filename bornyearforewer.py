bornyear = 0
while bornyear != 1799:
    bornyear = input('Введите год рождения А.С. Пушкина: ')
    if bornyear.isdigit():
        bornyear = int(bornyear)
        if bornyear == 1799:
            print('Верно')
        else:
            print('Неверно')
    else:
        print('Неверно')