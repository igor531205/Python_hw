# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем. Программа должна
# возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.


def user_input_fraction(message: str) -> list[int]:
    """Пользовательский ввод дроби.
    :param message: Сообщение пользователю.
    :return: Введенная пользователем дробь.
    """

    while True:

        _string = input(f'{message}')

        if _string.isdigit():

            _number = int(_string)

            if lower_limit <= _number <= upper_limit:

                return _number


message_for_user = f'Please enter a fraction in the format a/b -> '

fraction_from_user = user_input_fraction(message_for_user)
