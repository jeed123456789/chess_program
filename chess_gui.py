import tkinter
from tkinter import messagebox
from tkinter import PhotoImage
import chess


positions = []

def print_board(board_2d, chess_frame):
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
    position = ''
    piece_img_name = ''
    piece = ''
    for file in range(8):
        for rank in range(8):
            if board_2d[file][rank] != '.':
                piece = board_2d[file][rank]
                piece_img_name = piece_img[piece]+'.png'
                temp_img = PhotoImage(file = piece_img_name)
                position = chr(file+96)+str(8-rank)


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

def game_over(board):
    if board.is_stalemate() or board.is_insufficient_material() or board.is_game_over():
        return True
    else:
        return False

def make_move(board, uci):
    if chess.Move.from_uci(uci) in board.legal_moves:
        board.push_uci(uci)
        return True
    else:
        return False

def tell_position(btn_id):
     positions.append(btn_id)

def wants_to_quit(root):
    if messagebox.askokcancel(title = "Chess Program", detail = "Are you going to quit?"):
        root.destroy
    else:
        messagebox.showwarning(title = "Returning to Game", detail = "You will return back to your game")

board = chess.Board()
board_2d = change_2d(board)

root = tkinter.Tk()
root.title("Chess Program")
root.geometry("1000x500")

menubar = tkinter.Menu(root)
root['menu'] = menubar
menu_cmd = tkinter.Menu(menubar, tearoff = 0)
menu_help = tkinter.Menu(menubar, tearoff = 0)
menubar.add_cascade(menu = menu_cmd, label = 'Commands')
menubar.add_cascade(menu = menu_help, label = "Help")
menu_cmd.add_command(label = 'Quit', command = wants_to_quit(root))
menu_cmd.add_command(label = 'Help')



chess_frame = tkinter.Frame(root, height = 500, width = 500, relief = 'sunken', bd = 2, bg = '#D9E5FF')
chess_frame.pack(side = 'left', expand = True, fill = 'both')
action_frame = tkinter.Frame(root, height = 500, width = 500, relief = 'sunken', bd = 2, bg = '#D9E5FF')
action_frame.pack(side = 'left', expand = True, fill = 'both')

#, command = tell_position('a8')

a8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
a8.grid(row = 0, column = 0)
b8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
b8.grid(row = 0, column = 1)
c8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
c8.grid(row = 0, column = 2)
d8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
d8.grid(row = 0, column = 3)
e8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
e8.grid(row = 0, column = 4)
f8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
f8.grid(row = 0, column = 5)
g8 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
g8.grid(row = 0, column = 6)
h8 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
h8.grid(row = 0, column = 7)

a7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
a7.grid(row = 1, column = 0)
b7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
b7.grid(row = 1, column = 1)
c7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
c7.grid(row = 1, column = 2)
d7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
d7.grid(row = 1, column = 3)
e7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
e7.grid(row = 1, column = 4)
f7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
f7.grid(row = 1, column = 5)
g7 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
g7.grid(row = 1, column = 6)
h7 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
h7.grid(row = 1, column = 7)

a6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
a6.grid(row = 2, column = 0)
b6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
b6.grid(row = 2, column = 1)
c6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
c6.grid(row = 2, column = 2)
d6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
d6.grid(row = 2, column = 3)
e6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
e6.grid(row = 2, column = 4)
f6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
f6.grid(row = 2, column = 5)
g6 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
g6.grid(row = 2, column = 6)
h6 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
h6.grid(row = 2, column = 7)

a5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
a5.grid(row = 3, column = 0)
b5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
b5.grid(row = 3, column = 1)
c5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
c5.grid(row = 3, column = 2)
d5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
d5.grid(row = 3, column = 3)
e5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
e5.grid(row = 3, column = 4)
f5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
f5.grid(row = 3, column = 5)
g5 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
g5.grid(row = 3, column = 6)
h5 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
h5.grid(row = 3, column = 7)

a4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
a4.grid(row = 4, column = 0)
b4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
b4.grid(row = 4, column = 1)
c4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
c4.grid(row = 4, column = 2)
d4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
d4.grid(row = 4, column = 3)
e4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
e4.grid(row = 4, column = 4)
f4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
f4.grid(row = 4, column = 5)
g4 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
g4.grid(row = 4, column = 6)
h4 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
h4.grid(row = 4, column = 7)

a3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
a3.grid(row = 5, column = 0)
b3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
b3.grid(row = 5, column = 1)
c3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
c3.grid(row = 5, column = 2)
d3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
d3.grid(row = 5, column = 3)
e3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
e3.grid(row = 5, column = 4)
f3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
f3.grid(row = 5, column = 5)
g3 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
g3.grid(row = 5, column = 6)
h3 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
h3.grid(row = 5, column = 7)

a2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
a2.grid(row = 6, column = 0)
b2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
b2.grid(row = 6, column = 1)
c2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
c2.grid(row = 6, column = 2)
d2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
d2.grid(row = 6, column = 3)
e2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
e2.grid(row = 6, column = 4)
f2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
f2.grid(row = 6, column = 5)
g2 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
g2.grid(row = 6, column = 6)
h2 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
h2.grid(row = 6, column = 7)

a1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
a1.grid(row = 7, column = 0)
b1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
b1.grid(row = 7, column = 1)
c1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
c1.grid(row = 7, column = 2)
d1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
d1.grid(row = 7, column = 3)
e1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
e1.grid(row = 7, column = 4)
f1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
f1.grid(row = 7, column = 5)
g1 = tkinter.Button(chess_frame, bg = 'green', width = 6, height = 3)
g1.grid(row = 7, column = 6)
h1 = tkinter.Button(chess_frame, bg = 'white', width = 6, height = 3)
h1.grid(row = 7, column = 7)


print_board(board_2d, chess_frame)


root.mainloop()
