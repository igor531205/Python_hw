# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


def user_input_number(message: str, lower_limit: int, upper_limit: int) -> int:
    """Пользовательский ввод.
    :param message: Сообщение пользователю.
    :param lower_limit: Начальное значение ввода.
    :param upper_limit: Конечное значение ввода.
    :return: Введенное пользователем число.
    """

    while True:

        _string = input(f'{message}')

        if _string.isdigit():

            _number = int(_string)

            if lower_limit <= _number <= upper_limit:

                return _number


LOWER_LIMIT = -100_000
UPPER_LIMIT = 100_000

message_for_user = f'Please enter an integer between {LOWER_LIMIT} and {UPPER_LIMIT} -> '

number_from_user = user_input_number(message_for_user, LOWER_LIMIT, UPPER_LIMIT)
