import velha_funcoes

board = velha_funcoes.new_game()
player = 1
played = []
win = 0
max_played = 9


while True:
    velha_funcoes.print_board(board, player)
    if win != 0:
        if win == 1:
            print("\033[32mPlayer 1 venceu!\033[m")
            break
        else:
            print("\033[31mPlayer 2 venceu!\033[m")
            break
    play = int(input("Player {}, enter a number: ".format(player)))
    if play not in played:
        played.append(play)
        board = velha_funcoes.shot(board, player, play)
        player += 1
    else:
        print("\033[31mJogada inválida\033[m")
        continue
    if player > 2:
        player = 1
    win = velha_funcoes.win(board)


