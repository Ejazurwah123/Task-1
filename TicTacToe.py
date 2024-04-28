import math

def Input_Human(matrix):
    while True:
        try:
            row = int(input("Enter row number (0, 1, or 2): "))
            col = int(input("Enter column number (0, 1, or 2): "))
            if (0 <= row <= 2) and (0 <= col <= 2): 
                if matrix[row][col] == None:
                    return row, col
            else:
                print("invalid move :( Try again.")
        except ValueError:
            print("invalid input")
            
def initial_b():
    matrix = [[None, None, None],
             [None, None, None],
             [None, None, None] ]
    return matrix

def Display_b(matrix):
    for row in matrix:
        print(" | ".join(cell if cell is not None else ' ' for cell in row))
        print("---------")
        

def Final(matrix):
    #columns,rows check for a winner
    for c in range(3):
        if matrix[c][0] == matrix[c][1] == matrix[c][2] != None:
            return True
        if matrix[0][c] == matrix[1][c] == matrix[2][c] != None:
            return True
    #diagonals check
    if matrix[0][0] == matrix[1][1] == matrix[2][2] != None:
        return True
    if matrix[0][2] == matrix[1][1] == matrix[2][0] != None:
        return True

    #if the board is full
    for row in matrix:
        for cell in row:
            if cell == None:
                return False
    return True

def Minimax(matrix, depth, maxPlayer):
    if Final(matrix)  or depth == 0:
        return heuristic(matrix), None
    
    if maxPlayer:
        maxeval = -math.inf
        bestMove = None
        
        for moves in count_action(matrix):
            eval, _ = Minimax(resultant_matrix(matrix, moves, x),depth-1, False)
            if eval > maxeval:
                maxeval = eval
                bestMove = moves
        return maxeval , bestMove
    
    else:
        mineval = math.inf
        bestMove = None
        for move in count_action(matrix):
            eval, _ = Minimax(resultant_matrix(matrix, move, o),depth-1, True)
            if eval < mineval:
                mineval = eval
                bestMove = move
            return mineval , bestMove


def heuristic(matrix):
    if Final(matrix) != True:
        raise ValueError("Game still not finished")
    else:
        for person in [x,o]:
            for c in range(3):
                #checking for each row and cols
                if matrix[c][0] == matrix[c][1] == matrix[c][2] == person:
                        if person == x:
                            return 1
                        else:
                            return -1
                        
                if matrix[0][c] == matrix[1][c] == matrix[2][c] == person:
                        if person == x:
                            return 1
                        else:
                            return -1
            #checking for diagonals
            if matrix[0][0] == matrix[1][1] == matrix[2][2] == person:
                        if person == x:
                            return 1
                        else:
                            return -1
           
            if matrix[0][2] == matrix[1][1] == matrix[2][0] == person:
                        if person == x:
                            return 1
                        else:
                            return -1
               
        return 0
                
        
            
def count_action(matrix):
    emp_cell = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == None:
                emp_cell.append((i,j))
    return emp_cell
#returns list of all empty cells 


def resultant_matrix(matrix, move, player):
    i, j = move
    newmatrix = [row[:] for row in matrix]
    newmatrix[i][j] = player
    return newmatrix
    
def game():
    matrix = initial_b()
    print("Tic Tac Toe!")
    Display_b(matrix)

    while not Final(matrix):
        if len(count_action(matrix)) == 9:
            player = x
        else:
            if len(count_action(matrix)) % 2:
                player = o
            else:
                player = x

        if player == x:
            print("Player X's turn")
            row, col = Input_Human(matrix)
            matrix = resultant_matrix(matrix, (row, col), player)
        else:
            print("Player O's turn")
            _, move = Minimax(matrix, 9, True)
            board = resultant_matrix(matrix, move, player)
        Display_b(matrix)

    winner = heuristic(matrix)
    if winner == 1:
        print("Player X Wins :) ")
    elif winner == -1:
        print("Player O Wins :) ")
    else:
        print("It's a Draw :( ")

if __name__ == "__main__":
    # initialising player x and player y
    x = 'X'
    o = 'O'
    game()