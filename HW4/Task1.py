# Напишите функцию для транспонирования матрицы.


def matrix_transposition(matrix):
    """Функция транспонирования матрицы."""
    return list(list(i) for i in zip(*matrix))


MATRIX = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f'Old {MATRIX = }')
print(f'New MATRIX = {matrix_transposition(MATRIX)}')
