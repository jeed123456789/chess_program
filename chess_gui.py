# import important modules to run this program: tkinter, chess, and PIL
import tkinter
from tkinter import PhotoImage
import chess
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk

board = chess.Board() # initialize chess board in the start of a game
positions = [] # intialize list that will have all the buttons/positions pushed later used for making uci
num_moves = 0 # initialize num_moves to keep track of how many moves were made in total both white and black

# function to print the board, given the board_2d
# go through the matrixed board then go through every single square in the board and update the chess piece image on every square.
def print_board(board_2d, chess_frame, board_btn):
    # dictionary to get the name of the chess piece's png file
    piece_img = {
        "b":"bb",
        "B":"bw",
        "k":"kb",
        "K":"kw",
        "n":"nb",
        "N":"nw",
        "p":"pb",
        "P":"pw",
        "q":"qb",
        "Q":"qw",
        "r":"rb",
        "R":"rw"
        }
    piece_img_name = '' # create an empty string to create the file name of the chess piece_img
    piece = '' # the name of the piece in matrized board ex) b, B, k, K, n, N, etc

    # for loop to go through every single square in the board_2d and "print" the board
    for file in range(8):
        for rank in range(8):
            chess_btn = board_btn[file][rank]  # initialize chess_btn which is the button of a specific file and rank
            if board_2d[file][rank] != '.': # if statement to check if there is a piece in the square, empty squares are '.'
                piece = board_2d[file][rank]
                piece_img_name = 'img_chess/'+piece_img[piece]+'.png'
                # create temp_img to resize png file and display on the button
                temp_img = Image.open(piece_img_name)
                temp_img = temp_img.resize((45,44), Image.LANCZOS)
                photoImg = ImageTk.PhotoImage(temp_img)
                chess_btn.image = photoImg
                chess_btn.configure(image = photoImg, height = 50, width = 46)
            else:
                # if there is no piece, get rid of the image on the button
                chess_btn.image = ''
                chess_btn.configure(image = '', height = 3, width = 6)

# funciton to convert board to a matrix
# convert board into a string then into a matrix
def change_2d(board):
    ascii_board = str(board)
    board_2d = []
    rank = []
    for index in range(0,len(ascii_board),2):
        rank.append(ascii_board[index])
        if(index%16 == 14):
            board_2d.append(rank)
            rank = []
    return board_2d

# function for creating uci from buttons pushed and "pushing" move in board
def make_move(positions, board):
    global num_moves # global variable to take care of unboundlocal error

    initial_pos = positions[num_moves-2] # initialize initial_pos that will be connected to the "initial" button that has been pushed
    final_pos = positions[num_moves-1] # initialize final_pos that will be connected to the "final" button that has been pushed
    uci =  initial_pos + final_pos # uci is created by adding the starting square and the final squares

    # if statement for checking if uci is an invalid uci
    # if it is invalid, remove the two entries of buttons pushed and subtract 2 from num_moves
    if initial_pos == final_pos:
        positions.remove(initial_pos)
        positions.remove(final_pos)
        num_moves-=2
        return False

    # if statement to check if the move can be made
    # if it can be made, update the board and refresh the window
    # if not, remove two entries of buttons pushed and subtract 2 from num_moves
    if not board.is_game_over():
        if not chess.Move.from_uci(uci) in board.legal_moves:
            positions.remove(initial_pos)
            positions.remove(final_pos)
            num_moves-=2
            return False
        else:
            board.push_uci(uci)
            board_2d = change_2d(board)
            print_board(board_2d, chess_frame, board_btn)

            # check if there is stalemate, insufficient material, or checkmate in the board, if there any of those create messagebox and destroy window
            if board.is_stalemate():
                tkinter.messagebox.showinfo(title = 'Game ended', message = 'Stalemate')
                root.destroy()
            elif board.is_insufficient_material():
                tkinter.messagebox.showinfo(title = 'Game ended', message = 'Insufficient material')
                root.destroy()
            elif board.is_checkmate():
                if chess.WHITE: # determine which side won or lost
                    tkinter.messagebox.showinfo(title = 'Game ended', message = 'Black lost. White won.')
                    root.destroy()
                else: # determine which side won or lost
                    tkinter.messagebox.showinfo(titel = 'Game ended', message = 'White lost. Black won.')
                    root.destroy()
            elif board.is_check(): # check if there is a check
                tkinter.messagebox.showinfo(title = 'Check', message = 'Check')
            return True


# function that will be called when buttons are pushed, increments num_moves and adds the name of the button id in positions
def tell_position(btn_id):
    global num_moves
    positions.append(btn_id)
    num_moves+=1
    if num_moves%2 == 0 and num_moves != 0: # if statement for making move every time num_moves is divisible by 2.
        if not make_move(positions, board): # if make_move returns False, an illegal move was made, messagebox that talks about illegal move is posted.
            tkinter.messagebox.showinfo(title = 'Illegal move', message = 'That is an illegal move')

# function for when reset_game is pressed from the menu bar
def reset_game(board):
    board.reset()
    board_2d = change_2d(board)
    print_board(board_2d, chess_frame, board_btn)

# function for when help is pressed from the menu bar
def offer_help():
    tkinter.messagebox.showinfo(title = 'Help', message = 'No help can be given in a fair game of chess')

# create root window for program, set title and size
root = tkinter.Tk()
root.title("Chess Program")
root.geometry("420x450")

# create frame for where the board will stay in
chess_frame = tkinter.Frame(root, height = 500, width = 420, relief = 'sunken', bd = 2, bg = '#D9E5FF')
#chess_frame.pack(side = 'left', expand = True, fill = 'both')

# create button for each square in the board, the background, width, height, and bide command each button to tell_position
# then place the button in appropiate grid to resemble a chess board
a8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('a8'))
a8.grid(row = 0, column = 0)
b8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('b8'))
b8.grid(row = 0, column = 1)
c8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('c8'))
c8.grid(row = 0, column = 2)
d8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('d8'))
d8.grid(row = 0, column = 3)
e8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('e8'))
e8.grid(row = 0, column = 4)
f8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('f8'))
f8.grid(row = 0, column = 5)
g8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('g8'))
g8.grid(row = 0, column = 6)
h8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('h8'))
h8.grid(row = 0, column = 7)

a7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('a7'))
a7.grid(row = 1, column = 0)
b7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('b7'))
b7.grid(row = 1, column = 1)
c7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('c7'))
c7.grid(row = 1, column = 2)
d7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('d7'))
d7.grid(row = 1, column = 3)
e7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('e7'))
e7.grid(row = 1, column = 4)
f7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('f7'))
f7.grid(row = 1, column = 5)
g7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('g7'))
g7.grid(row = 1, column = 6)
h7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('h7'))
h7.grid(row = 1, column = 7)

a6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('a6'))
a6.grid(row = 2, column = 0)
b6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('b6'))
b6.grid(row = 2, column = 1)
c6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('c6'))
c6.grid(row = 2, column = 2)
d6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('d6'))
d6.grid(row = 2, column = 3)
e6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('e6'))
e6.grid(row = 2, column = 4)
f6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('f6'))
f6.grid(row = 2, column = 5)
g6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('g6'))
g6.grid(row = 2, column = 6)
h6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('h6'))
h6.grid(row = 2, column = 7)

a5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('a5'))
a5.grid(row = 3, column = 0)
b5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('b5'))
b5.grid(row = 3, column = 1)
c5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('c5'))
c5.grid(row = 3, column = 2)
d5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('d5'))
d5.grid(row = 3, column = 3)
e5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('e5'))
e5.grid(row = 3, column = 4)
f5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('f5'))
f5.grid(row = 3, column = 5)
g5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('g5'))
g5.grid(row = 3, column = 6)
h5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('h5'))
h5.grid(row = 3, column = 7)

a4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('a4'))
a4.grid(row = 4, column = 0)
b4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('b4'))
b4.grid(row = 4, column = 1)
c4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('c4'))
c4.grid(row = 4, column = 2)
d4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('d4'))
d4.grid(row = 4, column = 3)
e4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('e4'))
e4.grid(row = 4, column = 4)
f4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('f4'))
f4.grid(row = 4, column = 5)
g4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('g4'))
g4.grid(row = 4, column = 6)
h4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('h4'))
h4.grid(row = 4, column = 7)

a3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('a3'))
a3.grid(row = 5, column = 0)
b3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('b3'))
b3.grid(row = 5, column = 1)
c3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('c3'))
c3.grid(row = 5, column = 2)
d3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('d3'))
d3.grid(row = 5, column = 3)
e3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('e3'))
e3.grid(row = 5, column = 4)
f3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('f3'))
f3.grid(row = 5, column = 5)
g3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('g3'))
g3.grid(row = 5, column = 6)
h3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('h3'))
h3.grid(row = 5, column = 7)

a2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('a2'))
a2.grid(row = 6, column = 0)
b2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('b2'))
b2.grid(row = 6, column = 1)
c2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('c2'))
c2.grid(row = 6, column = 2)
d2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('d2'))
d2.grid(row = 6, column = 3)
e2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('e2'))
e2.grid(row = 6, column = 4)
f2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('f2'))
f2.grid(row = 6, column = 5)
g2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('g2'))
g2.grid(row = 6, column = 6)
h2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('h2'))
h2.grid(row = 6, column = 7)

a1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('a1'))
a1.grid(row = 7, column = 0)
b1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('b1'))
b1.grid(row = 7, column = 1)
c1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('c1'))
c1.grid(row = 7, column = 2)
d1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('d1'))
d1.grid(row = 7, column = 3)
e1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('e1'))
e1.grid(row = 7, column = 4)
f1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('f1'))
f1.grid(row = 7, column = 5)
g1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3, command = lambda:tell_position('g1'))
g1.grid(row = 7, column = 6)
h1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3, command = lambda:tell_position('h1'))
h1.grid(row = 7, column = 7)

# create board_btn, a matrix that can reference to every button/square in the board
board_btn = [[a8, b8, c8, d8, e8, f8, g8, h8],
                [a7, b7, c7, d7, e7, f7, g7, h7],
                [a6, b6, c6, d6, e6, f6, g6, h6],
                [a5, b5, c5, d5, e5, f5, g5, h5],
                [a4, b4, c4, d4, e4, f4, g4, h4],
                [a3, b3, c3, d3, e3, f3, g3, h3],
                [a2, b2, c2, d2, e2, f2, g2, h2],
                [a1, b1, c1, d1, e1, f1, g1, h1]]

# initialize the board for the first time and "print" board
board_2d = change_2d(board)
print_board(board_2d, chess_frame,board_btn)

# create menubar and bind commands to them
menubar = tkinter.Menu(root)
root['menu'] = menubar
menu_cmd = tkinter.Menu(menubar, tearoff = 0)
menu_help  = tkinter.Menu(menubar, tearoff = 0)
menubar.add_cascade(menu = menu_cmd, label = 'Commands')
menubar.add_cascade(menu = menu_help, label = 'Help')
menu_cmd.add_command(label = 'Quit', command =root.destroy)
menu_cmd.add_command(label = 'Reset Game', command = lambda:reset_game(board))
menu_help.add_command(label = 'Help', command = offer_help)

root.mainloop()
