# Tic-Tac-Toe Game in python
# Source code at https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874


def print_board(self, board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# This is main function of this game
def game(self):
    theBoard = {'7':'','8':'','9':'',
                '4':'','5':'','6':'',
                '1':'','2':'','3':''}

    turn = 'X'
    count = 0

    for i in range(10):
        print_board(theBoard)
        print("It's your tun, " + turn + ". Move to which place?")

        move = input()

        if move < 1 or move > 9:
            print('Please choose a valid position.')
            continue
        elif theBoard[move] == '':
            theBoard[move] = turn
            count += 1
        else:
            print('That position is already filled. Please choose another position.')
            continue

        # Now we will check if a player has won the game after every move post 5 moves
        if count>=5:
            if theBoard[7] == theBoard[8] == theBoard[9] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            elif theBoard[4] == theBoard[5] == theBoard[6] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            elif theBoard[1] == theBoard[2] == theBoard[3] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            elif theBoard[7] == theBoard[4] == theBoard[1] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            elif theBoard[8] == theBoard[5] == theBoard[2] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            elif theBoard[9] == theBoard[6] == theBoard[3] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            elif theBoard[7] == theBoard[5] == theBoard[3] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            elif theBoard[9] == theBoard[5] == theBoard[1] != '':
                print_board()
                print('\nGame Over\n')
                print('**** {turn} has won *****')
                break
            else:
                #Change turn after every move
                if turn == 'X':
                    turn = '0'
                else:
                    turn = 'X'
            
                # If game draws
                if count == 9:
                    print_board()
                    print('\nGame Over\n')
                    print('**** No one has won. Game is a draw. *****')
                    break

    restart_game = input('Do you wish to play again? (y/n): ')
    if restart_game.upper() == 'Y':
        game()

if __name__ == "__main__":
    game()