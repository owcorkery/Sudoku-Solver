board = [
    [1,7,9,6,0,3,5,0,4],
    [5,8,6,4,0,0,1,9,0],
    [0,2,4,9,0,5,0,0,0],
    [0,0,0,2,0,0,9,0,0],
    [0,0,0,0,7,0,0,3,0],
    [8,0,0,3,0,0,0,0,6],
    [0,0,0,1,3,2,0,4,0],
    [0,0,1,7,6,0,0,0,8],
    [7,0,0,5,9,8,0,1,2]
]


# Uses recursive backtracking to go through every possible value being put in every spot and returns the correct board
def solve(b):

    empty_spot = find_empty(b)

    if empty_spot[0] == 10 and empty_spot[1] == 10:
        return True
    else:
        row = empty_spot[0]
        col = empty_spot[1]
    
    for i in range(1,10):
        if is_allowed(b, i, row, col) == True:
            b[row][col] = i
        
            if solve(b) == True:
                return True
        
            b[row][col] = 0

    return False


# Checks each row, column, and box to make sure that the number being inserted hasn't been used before
def is_allowed(b, val, row, col):
    for i in range(len(b)):
        if(b[i][col] == val and row != i):
            return False
        
    for j in range(len(b[0])):
        if(b[row][j] == val and col != j):
            return False

    new_row = row // 3
    new_col = col // 3

    for i in range(new_row * 3, new_row * 3 + 3):
        for j in range(new_col * 3, new_col * 3  + 3):
            if(b[i][j] == val and i != row and j != col):
                return False

    return True



# Finds a spot on the board that has not been filled in yet
def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                position = [i,j]
                return position
    
    position = [10,10]
    return position




# This function prints out the sudoku board
def print_board(b):
    for i in range(len(b)):
        
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        
        for j in range(len(b[0])):

            if j % 3 == 0 and j != 0:
                print("| ", end = "")
            
            if j == len(b[0]) - 1:
                print(b[i][j])
            else:
                print(b[i][j], end = " ")


print_board(board)
solve(board)
print("______________________________________ \n")
print_board(board)