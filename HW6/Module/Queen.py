def is_win(arrangements: list) -> bool:

    size_of_chessboard = 8
    chessboard_x = []
    chessboard_y = []

    for position in range(size_of_chessboard):
        x, y = arrangements[position]
        chessboard_x.append(x)
        chessboard_y.append(y)

    for i in range(size_of_chessboard):
        for j in range(i + 1, size_of_chessboard):
            if chessboard_x[i] == chessboard_x[j] or chessboard_y[i] == chessboard_y[j] \
                    or abs(chessboard_x[i] - chessboard_x[j]) == abs(chessboard_y[i] - chessboard_y[j]):
                return True
    return False


def chessboard_random_position(count_arrangements: int) -> list:

    pass
