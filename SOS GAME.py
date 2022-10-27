P1Score, P2Score, w, h = 0, 0, 4, 4
cellsUsed = 0
P1Turn, gameOver = True, False
Matrix = [["." for x in range(w)] for y in range(h)]
posX, posY = 0, 0
countExistingSOS = 0


def is_game_over():
    #If all cells in the board are used,then players can no longer play
    if cellsUsed != w * h:
        return False
    # Since all cells in the board are used,then players can no longer play
    print("########Game Over#########")
    #If all cells in the game are not used then players can continue playing and game isn't over
    if P1Score > P2Score:
        print("Player 1 Won")
    elif P2Score > P1Score:
        print("Player 2 Won")
    else:
        print("It's a draw")
    print("P1:", P1Score, " P2:", P2Score)
    return True


def print_matrix():
    for i in reversed(range(h)):
        str1 = str(i+1)+""
        for j in range(w):
            str1 += Matrix[j][i]
        print(str1)

    print(" 1234")
    print("########Score#########")
    print("P1:", P1Score, " P2:", P2Score)


def fill_cell():
    player = ""
    if P1Turn:
        player = "Player1"
    else:
        player = "Player2"
    coordinate = "(" + str(posX) + "," + str(posY) + ")"
    value = input(player + ": Enter S or O in coordinate of your square" + coordinate)
    while True:
        #Enters valid input
        if value == "S" or value == "O":
            Matrix[posX - 1][posY - 1] = value
            break
        else:
            value = eval(
                input("Incorrect input " + player + ": Enter S or O in coordinate of your square" + coordinate))


def take_input():
    player = ""
    if P1Turn:
        player = "Player1"
    else:
        player = "Player2"
    global posX, posY
    posX = int(input(player + ": Choose the X coordinate of your square"))
    posY = int(input(player + ": Choose the Y coordinate of your square"))

    # Continues to ask user for input until they enter valid input
    while True:
        # posX has to be between 1 and 4
        if posX > 4 or posX < 1:
            posX = int(input("Enter a number between 1 and 4 for the X coordinate"))
        # posY has to be between 1 and 4
        elif posY > 4 or posY < 1:
            posY = int(input("Enter a number between 1 and 4 for the Y coordinate"))
        # Cell in posX,posY has to be empty
        elif Matrix[posX - 1][posY - 1] != ".":
            posX = int(input("This cell is taken. Enter the new X coordinate"))
            posY = int(input("This cell is taken. Enter the new Y coordinate"))
        # User finally gave correct input for coordinate
        # Time to know whether they want an 'S' or an 'O'
        else:
            # Call method that enters s/o in the grid
            fill_cell()
            break


def countAllSOS():
    countSOS = 0
    for i in range(w):
        for j in range(h):
            # in lower left quadrant ^>
            if i <= 1 and j <= 1:
                # Going upwards
                if Matrix[i][j] == 'S' and Matrix[i][j + 1] == 'O' and Matrix[i][j + 2] == 'S':
                    countSOS += 1
                # Going right
                if Matrix[i][j] == 'S' and Matrix[i + 1][j] == 'O' and Matrix[i + 2][j] == 'S':
                    countSOS += 1
                # Going diagonal / upwards and right
                if Matrix[i][j] == 'S' and Matrix[i + 1][j + 1] == 'O' and Matrix[i + 2][j + 2] == 'S':
                    countSOS += 1
            # in lower right quadrant <^
            elif i > 1 and j <= 1:
                # Going upwards
                if Matrix[i][j] == 'S' and Matrix[i][j + 1] == 'O' and Matrix[i][j + 2] == 'S':
                    countSOS += 1
                # Going left
                if Matrix[i][j] == 'S' and Matrix[i - 1][j] == 'O' and Matrix[i - 2][j] == 'S':
                    countSOS += 1
                # Going diagonal \ upwards and left
                if Matrix[i][j] == 'S' and Matrix[i - 1][j + 1] == 'O' and Matrix[i - 2][j + 2] == 'S':
                    countSOS += 1
            # in upper right quadrant <v
            elif i > 1 and j > 1:
                # Going downwards
                if Matrix[i][j] == 'S' and Matrix[i][j - 1] == 'O' and Matrix[i][j - 2] == 'S':
                    countSOS += 1
                # Going left
                if Matrix[i][j] == 'S' and Matrix[i - 1][j] == 'O' and Matrix[i - 2][j] == 'S':
                    countSOS += 1
                # Going diagonal / downwards and left
                if Matrix[i][j] == 'S' and Matrix[i - 1][j - 1] == 'O' and Matrix[i - 2][j - 2] == 'S':
                    countSOS += 1
            # in upper left quadrant v>
            elif i <= 1 and j > 1:
                # Going downwards
                if Matrix[i][j] == 'S' and Matrix[i][j - 1] == 'O' and Matrix[i][j - 2] == 'S':
                    countSOS += 1
                # Going right
                if Matrix[i][j] == 'S' and Matrix[i + 1][j] == 'O' and Matrix[i + 2][j] == 'S':
                    countSOS += 1
                # Going diagonal \ downwards and right
                if Matrix[i][j] == 'S' and Matrix[i + 1][j - 1] == 'O' and Matrix[i + 2][j - 2] == 'S':
                    countSOS += 1
    return countSOS//2

while not is_game_over():
    if P1Turn:
        # Player 1 plays
        print_matrix()
        take_input()
        # Get latest Count of all SOS on the board
        latestCountSOS = countAllSOS()
        # Subtract count of SOS from last play to get new SOSes from this turn
        newCountSOSFromNewCell = latestCountSOS - countExistingSOS
        # Update count ofExisting SOSes to be used in next play
        countExistingSOS = latestCountSOS
        P1Score += newCountSOSFromNewCell
        if newCountSOSFromNewCell == 0:
            P1Turn = False
    #     did last input form an SOS
    else:
        # Player 2 plays
        print_matrix()
        take_input()
        # Get Count of all SOS on the board
        latestCountSOS = countAllSOS()
        # Subtract count of SOS from last play to get new SOSes from this turn
        newCountSOSFromNewCell = latestCountSOS - countExistingSOS
        # Update count ofExisting SOSes to be used in next play
        countExistingSOS = latestCountSOS
        P2Score += newCountSOSFromNewCell
        if newCountSOSFromNewCell == 0:
            P1Turn = True
    cellsUsed += 1
