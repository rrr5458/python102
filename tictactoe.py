board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]
row_index = 0
for i in board: 
    col_index = 0
    for j in i:
        print(j, end = " ")
    print(" ")

row_choice_O = int(input("Move row? "))
col_choice_O = int(input("Move column? "))
board[row_choice_O][col_choice_O] = "0"

row_index = 0
for i in board: 
    col_index = 0
    for j in i:
        print(j, end = " ")
    print(" ")

row_choice_X = int(input("Move row? "))
col_choice_X = int(input("Move column? "))
board[row_choice_X][col_choice_X] = "X"

row_index = 0
for i in board: 
    col_index = 0
    for j in i:
        print(j, end = " ")
    print(" ")



