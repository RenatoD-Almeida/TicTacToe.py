def new_game():
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return board


def print_jogador(player):
    if player == 1:
        return f'\033[32mJogador 1: X\033[m   Jogador 2: 0'
    else:
        return f'Jogador 1: X   \033[31mJogador 2: 0\033[m'


def print_board(board, player):
    print("Jogo da velha".center(30))
    print("""{}
 {} | {} | {}
===+===+===
 {} | {} | {}
===+===+===
 {} | {} | {}
    """.format(print_jogador(player),
               board[0][0], board[0][1], board[0][2],
               board[1][0], board[1][1], board[1][2],
               board[2][0], board[2][1], board[2][2], ))


def shot(board, player, play):
    if player == 1:
        choice = f"\033[32m{'X'}\033[m"
    else:
        choice = f'\033[31m{"O"}\033[m'

    if play == 1:
        board[0][0] = choice
    elif play == 2:
        board[0][1] = choice
    elif play == 3:
        board[0][2] = choice
    elif play == 4:
        board[1][0] = choice
    elif play == 5:
        board[1][1] = choice
    elif play == 6:
        board[1][2] = choice
    elif play == 7:
        board[2][0] = choice
    elif play == 8:
        board[2][1] = choice
    else:
        board[2][2] = choice
    return board


def win(board):
    ''' sequencia de linhas '''
    # Linha 0
    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    # Linha 1
    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    # Linha 2
    if board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    '''Sequencia de colunas'''
    # Coluna 0
    if board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    # Coluna 1
    if board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    # Coluna 2
    if board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    '''Sequencia de diagonais'''
    # Diagonal principal
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    # Diagonal secundária
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == f"\033[32m{'X'}\033[m":
            return 1
        else:
            return 2

    return 0