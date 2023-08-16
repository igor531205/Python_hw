# Треугольник существует только тогда, когда сумма любых двух его сторон больше
# третьей. Дано a, b, c — стороны предполагаемого треугольника. Требуется
# сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в
# одном случае отрезок окажется больше суммы двух других, то треугольника с
# такими сторонами не существует. Отдельно сообщить является ли треугольник
# разносторонним, равнобедренным или равносторонним.


def user_input_number(side: str, lower_limit: int, upper_limit: int) -> int:
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :param lower_limit: Начальное значение ввода.
    :param upper_limit: Конечное значение ввода.
    :return: Введенное пользователем число.
    """

    message = f'Please enter a side "{side}" of triangle from {lower_limit}'\
        + f' to {upper_limit} -> '

    number = None
    while number is None:

        string = input(f'{message}')

        if string.isdigit():

            temp_number = int(string)

            if lower_limit <= temp_number <= upper_limit:

                number = temp_number

    return number


def triangle_check(triangle: dict) -> str:
    """Проверка треугольника.
    :param triangle: Стороны треугольника.    
    :return: Результат проверки.
    """

    def check_is_triangle(triangle: dict) -> bool:
        """Проверка что треугольник существует.
        :param triangle: Стороны треугольника.    
        :return: Результат проверки.
        """

        NUMBER_OF_SIDES_TRIANGLE = 3
        number_of_sides = len(triangle.values())

        if number_of_sides > NUMBER_OF_SIDES_TRIANGLE:

            return False

        perimeter = sum(triangle.values())

        for value in triangle.values():

            other_sides = perimeter - value

            if value >= other_sides:

                return False

        return True

    def triangle_type(triangle: dict) -> str:
        """Проверка типа треугольника.
        :param triangle: Стороны треугольника.    
        :return: Тип треугольника.
        """

        # number_of_equal_sides = int()

        # sides = list([value for value in triangle.values()])

        # number_of_sides = len(sides)

        # perimeter = sum(sides)

        # for side in range(number_of_sides):

        #     other_sides = perimeter - sides[side]

        # if value >= other_sides:
        #     sides[side]

        # if number_of_sides > 3:
        # return f'Such a triangle does not exist.'

        # perimeter = sum(triangle.values())

        # number_of_equal_sides = int()

        # for key, value in triangle.items():

        #     other_sides = perimeter - value

        #     if value >= other_sides:

        #         return f'Such a triangle does not exist.'

        #     for key_in, value_in in triangle.items():

        #         if key != key_in and value == value_in:

        #             number_of_equal_sides += 1

        # if number_of_equal_sides == 0:

        #     return f'Triangle scalene.'

        # elif number_of_equal_sides == 1:

        #     return f'Triangle isosceles.'
        # elif number_of_equal_sides == 2:
        #     return f'Triangle is equilateral.'

    if check_is_triangle(triangle):

        return triangle_type(triangle)

    else:
        return f'Such a triangle does not exist.'


LOWER_LIMIT = 0
UPPER_LIMIT = 1000

A = 'a'
B = 'b'
C = 'c'

triangle = {
    A: user_input_number(A, LOWER_LIMIT, UPPER_LIMIT),
    B: user_input_number(B, LOWER_LIMIT, UPPER_LIMIT),
    C: user_input_number(C, LOWER_LIMIT, UPPER_LIMIT),
}

result_triangle_check = triangle_check(triangle)

print(f'{result_triangle_check}')
