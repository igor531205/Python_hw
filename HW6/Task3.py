# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.​


from Module.Queen import chessboard_rundom_not_win_position


if __name__ == '__main__':

    NEAD_NUMBER_OF_POSITIONS = 4
    arrangements = [chessboard_rundom_not_win_position() for _ in range(NEAD_NUMBER_OF_POSITIONS)]
    print(*arrangements, sep='\n')
