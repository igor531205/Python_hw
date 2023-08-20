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

        _fraction_args = _string[1::].split('/') if _string[0] == '-' else _string.split('/')

        _COUNT_OF_ARGUMENTS_FRACTION = 2

        if len(_fraction_args) == _COUNT_OF_ARGUMENTS_FRACTION and all(a.isdigit() for a in _fraction_args):

            return _string

        else:
            print('You entered a fraction in the wrong format')


def fraction_sum(fraction_1: str, fraction_2: str) -> str:
    """Суммирование дробей.
    :param fraction_1: Первая дробь.
    :param fraction_2: Вторая дробь.
    :return: Сумма дробей.
    """

    NUMERATOR_INDEX = 0
    DENOMINATOR_INDEX = 1

    _fraction_args_1 = [int(val) for val in fraction_1.split('/')]
    _fraction_args_2 = [int(val) for val in fraction_2.split('/')]

    if _fraction_args_1[DENOMINATOR_INDEX] == _fraction_args_2[DENOMINATOR_INDEX]:

        _fraction_res_numerator = _fraction_args_1[NUMERATOR_INDEX] + _fraction_args_2[NUMERATOR_INDEX]
        _fraction_res_denominator = _fraction_args_1[DENOMINATOR_INDEX]

        return f'{_fraction_res_numerator}/{_fraction_res_denominator}'

    else:

        _fraction_res_numerator = _fraction_args_1[NUMERATOR_INDEX] * _fraction_args_2[DENOMINATOR_INDEX] \
            + _fraction_args_2[NUMERATOR_INDEX] * _fraction_args_1[DENOMINATOR_INDEX]
        _fraction_res_denominator = _fraction_args_1[DENOMINATOR_INDEX] * _fraction_args_2[DENOMINATOR_INDEX]

        return f'{_fraction_res_numerator}/{_fraction_res_denominator}'


def fraction_multiply(fraction_1: str, fraction_2: str) -> str:
    """Суммирование дробей.
    :param fraction_1: Первая дробь.
    :param fraction_2: Вторая дробь.
    :return: Сумма дробей.
    """

    NUMERATOR_INDEX = 0
    DENOMINATOR_INDEX = 1

    _fraction_args_1 = [int(val) for val in fraction_1.split('/')]
    _fraction_args_2 = [int(val) for val in fraction_2.split('/')]

    _fraction_res_numerator = _fraction_args_1[NUMERATOR_INDEX] * _fraction_args_2[NUMERATOR_INDEX]
    _fraction_res_denominator = _fraction_args_1[DENOMINATOR_INDEX] * _fraction_args_2[DENOMINATOR_INDEX]

    return f'{_fraction_res_numerator}/{_fraction_res_denominator}'


message_for_user = f'Please enter a fraction in the format a/b -> '
fraction_from_user_1 = user_input_fraction(message_for_user)

message_for_user = f'Please enter a other fraction in the format a/b -> '
fraction_from_user_2 = user_input_fraction(message_for_user)

print(f'Result:\n{fraction_from_user_1} + {fraction_from_user_2} = '
      + f'{fraction_sum(fraction_from_user_1, fraction_from_user_2)}\n'
      + f'{fraction_from_user_1} * {fraction_from_user_2} = '
      + f'{fraction_multiply(fraction_from_user_1, fraction_from_user_2)}')

print(f'Result check:\n' + f'{fraction_from_user_1} + {fraction_from_user_2} = '
      + f'{Fraction(fraction_from_user_1) + Fraction(fraction_from_user_2)}\n'
      + f'{fraction_from_user_1} * {fraction_from_user_2} = '
      + f'{Fraction(fraction_from_user_1) * Fraction(fraction_from_user_2)}')
