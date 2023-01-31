from random import choice
from time import sleep

def exem_step ():
    stepx, stepy = input('Ваш ход. \nВведите координату по вертикали'), input('Введите координату по горизонтали')
    if len(stepx) == 1 and len(stepy) == 1 and 49 <= ord(stepx) <= 51 and 49 <= ord(stepy) <= 51:
        stepx, stepy = int(stepx), int(stepy)
    else:
        print('Координаты указаны не корректно, попробуйте еще раз. \nКоординаты должны указвать на свободную клетку поля')
        return (exem_step())
    if display[stepx][stepy] != '-':
        print('Клетка уже занята, выберете свободную')
        return (exem_step())
    else:
        return stepx, stepy

def print_display(display):
    for _ in range(4):
        print(*display[_])

def winner():
    for _ in range(1, 4):
        if display[1][_] == display[2][_] == display[3][_] != '-' or \
                display[_][1] == display[_][2] == display[_][3] != '-':
            return winner
    if display[1][1] == display[2][2] == display[3][3] != '-' or \
            display[1][3] == display[2][2] == display[3][1] != '-':
        return winner

win, lose, draw = 0, 0, 0
while True:
    display = [['-' for i in range(4)] for j in range(4)]
    random_dict = {(1, 1): 1, (1, 2): 2, (1, 3): 3, (2, 1): 4, (2, 2): 5, (2, 3): 6, (3, 1): 7, (3, 2): 8, (3, 3): 9}
    for i in range(4):
        display[i][0] = i
        display[0][i] = i
    count = 0

    start = input('Поиграем в крестики-нолики? \n(Yes/No)')
    if start == 'No':
        print('Жаль, буду ждать тебя в следующий раз..')
        break
    else:
        print(f'Начнем игру! \nОбщий счет: \nПобед: {win} \nПоражений: {lose} \nНичья: {draw}')
        print_display(display)

    while True:
        step = exem_step()
        display[step[0]][step[1]] = 'X'
        print_display(display)
        random_dict.pop(step)
        count += 1

        if winner():
            print('Это победа!')
            win += 1
            break
        if count == 9:
            print('Ничья')
            draw += 1
            break

        print('Мой ход...')
        sleep(1)
        step = choice(list(random_dict.keys()))
        display[step[0]][step[1]] = 'O'
        print_display(display)
        random_dict.pop(step)
        count += 1

        if winner():
            print('Поражение')
            lose += 1
            break
        if count == 9:
            print('Ничья')
            draw += 1
            break