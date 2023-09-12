# Создайте функцию генератор чисел Фибоначчи.


def fibonachi(_n: int):
    """Функция генератор чисел Фибоначчи."""

    f_1 = 0
    f_2 = 1

    if _n >= 0:

        while _n >= 0:

            yield f_1
            f_1, f_2 = f_2, f_1 + f_2
            _n -= 1

    else:

        while _n <= 0:

            yield f_1
            f_1, f_2 = f_2, f_1 - f_2
            _n += 1


print(*fibonachi(-10), sep='\t')
print(*fibonachi(0))
print(*fibonachi(10), sep='\t')
