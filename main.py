import velha_funcoes

board = velha_funcoes.new_game()
player = 1
played = [] # cada jogada será cadastrada aqui, para evitar jogadas repetidas
win = 0 # var que verifica se o jogo acabou
max_played = 9


while max_played > 0:
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
        max_played -= 1
    else:
        print("\033[31mJogada inválida\033[m")
        continue

    if player > 2:
        player = 1
    win = velha_funcoes.win(board)
else:
    print("\033[33m----- Empatou ------\033[m")