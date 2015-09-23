# Collisions are possible for two queens (i,j) and (row,col)
# i == row     (same row)
# j == col    (same column)
# row-i == col-j (same diagonal)

board = []


def collision(row, col):
    """ Return if there is a danger by placing queen in
        a given row, col
    """
    for (i, j) in board:
        if row == i:
            return True
        if col == j:
            return True
        if abs(row - i) == abs(col - j):
            return True

    return False

# board contains current possible values of row,col where the queen can
# reside without collision


def placequeen(row, size):
    if row > size:
        print_board(board, size)
    else:
        for col in range(1, size + 1):
            if not collision(row, col):
                board.append((row, col))
                # print " Append: row %s col %s" %(row,col)
                placequeen(row + 1, size)
                # print "Remove: row %s col %s" %(row,col)
                board.remove((row, col))


def print_board(board, size):
    output = []
    print " -------------------------"
    for row in range(1, size + 1):
        for col in range(1, size + 1):
            if (row, col) in board:
                output += "  Q"
            else:
                output += "  -"
        output += "\n"
    print "".join(output)

if __name__ == "__main__":
    placequeen(1, 4)
    # placequeen(1,8)
