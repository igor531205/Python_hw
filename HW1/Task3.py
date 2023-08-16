# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10
# попыток. Программа должна подсказывать «больше» или «меньше» после каждой
# попытки. Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint


def generation_random_number(lower_limit: int, upper_limit: int) -> int:
    """Генерация случайного числа.
    :param lower_limit: Начальное значение.
    :param upper_limit: Конечное значение.
    :return: Случайное число.
    """

    return randint(lower_limit, upper_limit)


def search_number(hidden_number: int, lower_limit: int, upper_limit: int,
                  attempts: int) -> str:
    """Поиск числа.
    :param hidden_number: Скрытое число.
    :param lower_limit: Начальное значение.
    :param upper_limit: Конечное значение.
    :param attempts: Количество попыток.
    :return: Результат поиска числа.
    """

    NEXT_NUMBER = 1

    for i in range(attempts):

        message_for_user = f'Please enter a natural number from {lower_limit}'\
            + f' to {upper_limit}. You have {attempts} attempts -> '

        number = user_input_number(message_for_user, lower_limit, upper_limit)

        if number == hidden_number:
            return f'Number guessed'

        elif number > hidden_number:
            print('You entered a number greater than the hidden number')
            upper_limit = number - NEXT_NUMBER

        elif number < hidden_number:
            print('You entered a number less than the hidden number')
            lower_limit = number + NEXT_NUMBER

        attempts -= NEXT_NUMBER

    return f'Number not guessed'


def user_input_number(message: str, lower_limit: int, upper_limit: int) -> int:
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :param lower_limit: Начальное значение ввода.
    :param upper_limit: Конечное значение ввода.
    :return: Введенное пользователем число.
    """

    number = None
    while number is None:

        string = input(f'{message}')

        if string.isdigit():

            temp_number = int(string)

            if lower_limit <= temp_number <= upper_limit:

                number = temp_number

    return number


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
NUMBER_OF_ATTEMPTS = 10

hidden_number = generation_random_number(LOWER_LIMIT, UPPER_LIMIT)

result = search_number(hidden_number, LOWER_LIMIT, UPPER_LIMIT,
                       NUMBER_OF_ATTEMPTS)

print(f'{result}, hidden number is {hidden_number}')
