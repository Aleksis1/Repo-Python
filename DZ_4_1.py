# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника

def sal():
    try:
        time = float(input('Отработано (часов): '))
        salary = int(input('Нормо/час (рублей): '))
        bonus = int(input('Премия (рублей): '))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника (рублей): {res}')
    except ValueError:
        return print('Not a number')


sal()
