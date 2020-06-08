# Tic-Tac-Toe Game in python
# Source code at https://medium.com/byte-tales/the-classic-tic-tac-toe-game-in-python-3-1427c68b8874


theBoard = {'7':'','8':'','9':'',
            '4':'','5':'','6':'',
            '1':'','2':'','3':''}

def print_board(self, board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# This is main function of this game
def game():
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
            count = count + 1
        else:
            print('That position is already filled. Please choose another position.')
            continue


    