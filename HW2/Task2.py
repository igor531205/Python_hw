# Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем и знаменателем. Программа должна
# возвращать сумму и *произведение дробей. Для проверки своего кода используйте модуль fractions.
# Ширина экрана 120 символов


from fractions import Fraction


def user_input_fraction(message: str) -> str:
    """Пользовательский ввод дроби.
    :param message: Сообщение пользователю.
    :return: Введенная пользователем дробь.
    """

    while True:

        _string = input(f'{message}')

        _fraction_arguments = _string[1::].split('/') if _string[0] == '-' else _string.split('/')
        print(_fraction_arguments)

        _COUNT_OF_ARGUMENTS_FRACTION = 2

        if len(_fraction_arguments) == _COUNT_OF_ARGUMENTS_FRACTION and all(a.isdigit() for a in _fraction_arguments):

            return _string

        else:
            print('You entered a fraction in the wrong format')


def fraction_sum(fraction_1: str, fraction_2: str) -> str:
    """Суммирование дробей.
    :param fraction_1: Первая дробь.
    :param fraction_2: Вторая дробь.
    :return: Сумма дробей.
    """


def fraction_multiply(fraction_1: str, fraction_2: str) -> str:
    """Суммирование дробей.
    :param fraction_1: Первая дробь.
    :param fraction_2: Вторая дробь.
    :return: Сумма дробей.
    """


message_for_user = f'Please enter a fraction in the format a/b -> '

fraction_from_user_1 = user_input_fraction(message_for_user)
fraction_from_user_2 = user_input_fraction(message_for_user)

print(f'Result:\n{fraction_from_user_1} + {fraction_from_user_2} = '
      + f'{fraction_sum(fraction_from_user_1, fraction_from_user_2)}\n'
      + f'{fraction_from_user_1} * {fraction_from_user_2} = '
      + f'{fraction_multiply(fraction_from_user_1, fraction_from_user_2)}')

print(f'Result check:\n' + f'{fraction_from_user_1} + {fraction_from_user_2} = '
      + f'{Fraction(fraction_from_user_1) + Fraction(fraction_from_user_2)}\n'
      + f'{fraction_from_user_1} * {fraction_from_user_2} = '
      + f'{Fraction(fraction_from_user_1) * Fraction(fraction_from_user_2)}')
