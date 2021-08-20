# Крестики нолики
# Глобальные константы
X = 'X'
O = 'O'
EMPTY = ' '  # представляет пустое поле на игровой доске
TIE = 'Ничья'  # Представляет состояние ничьей
NUM_SQUARES = 9  # Кол-во полей на доске


def display_instruction():
    '''Выводит инсерукцию для игрока'''
    print('''Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времён!
    Твой мозг и мой процессор сойдутся в схватке на доске игры "Крестики нолики".
    что бы сделать ход, введи число от 0 до 8. Числа однозначно соответствуют полям доски
    так как показано ниже:
    0|1|2
    -----
    3|4|5
    -----
    6|7|8
    Приготовся к бою, жалкий бестолковый человечишкаю вот вот начнется решающее сражение!!!\n''')


def ask_es_no(question):
    '''Задаёе вопрос, на "да" или "нет".Принимает введённый текст и возвращает "y" or "no"'''
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    '''проситв вести число из указанного диапазона(текст вопроса,нижний диапазон,верхний диапазон)'''
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    '''Определяет принадлежность первого хода человеку или компьютеру,
    возвращает у кого кретик или нолик '''
    go_first = ask_number('Хочешь оставить певый ход за собой? (y/n)')
    if go_first == 'y':
        print('у что ж, даю тебе фору: Играй крестиками')
        human, computer = X, O
    else:
        human, computer = O, X
    return computer, human


def new_board():
    '''Создаё тпустую игровую доску, возвращает доску'''
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    '''Отобржает игровую доску на экране,принимает доску'''
    print('/n/t', board[0], '|', board[1], '|', board[2])
    print('\t', '-------')
    print('/n/t', board[3], '|', board[4], '|', board[5])
    print('\t', '-------')
    print('/n/t', board[6], '|', board[7], '|', board[8])


def legal_moves(board):
    '''Создаёт список доступных ходов. Принимает доску. Возвращает список доступных ходов'''
    moves = []
    for i in range(NUM_SQUARES):
        if board[i] == EMPTY:
            moves.append(i)
    return moves


def winner(board):
    '''Определяет победителя игры. принимает доску. Возвращает
    тип фишек победителя:"ничья" или None'''
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]]:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE
    return None


def human_move(board, human):
    '''Узнаёт, какой ход желает совершить игрок. Принимает доску и тип фишек
    человека. Возвращает ход человека'''
    legal = legal_moves(board)
    move = 0
    while move not in legal:
        move = ask_number('Твой ход.Выбери одно из полей(0-8):', 0, NUM_SQUARES)
        if move not in legal:
            print('Это поле уже занято, выбери другоею\n')
    print('Ладно')
    return move


def computer_move(board, computer, human):
    '''Расчитывает ход компьютеного противника. Принимает доску,
    тип фишек компьютера и человека. Возвращает ход компьютера'''
    board = board[:]
    BEST_MOBES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    print("я выберу поле номер", end=' ')
    for move in legal_moves(board):
        board[move]


def next_turn(turn):
    '''Осуществляет переход к следующему ходу. Принимает тип фишекю.
    Возвращает тип фишек'''


def congrat_winner(the_winner, computer, human):
    '''Поздравляет победителя и констатирует ничью. принимает тип фишек победителя,
    тип фишек компьютера и человека'''
    print(('fools'))
    
