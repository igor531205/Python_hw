# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.
# Ширина экрана 120 символов


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


def dec_to_hex(number: int) -> str:
    """Преобразование десятичного числа в шестнадцатиричное строковое представление.
    :param number: Число в десятичном представлении.
    :return: Число в шестнадцатиричном строковом представлении.
    """

    def number_to_string_hex(_num: int) -> str:
        """Преобразование числа в строковое представление.
        :param num: Число.
        :return: Шестнадцатиричное строковое представление.
        """

        _HEX_ZERRO = 0
        _HEX_NUMBER_LEN = 9
        _HEX_FULL_LEN = 15
        _OFFSET_VALUES_IN_ASCII_TABLE = 87

        if _HEX_ZERRO <= _num <= _HEX_NUMBER_LEN:
            return str(_num)

        elif _HEX_NUMBER_LEN < _num <= _HEX_FULL_LEN:
            return chr(_num + _OFFSET_VALUES_IN_ASCII_TABLE)

        else:
            return 'error'

    _CONVERSION_FACTOR_HEX: int = 16
    _remainders = list()

    while number > 0:

        number, _temp_remainder = divmod(number, _CONVERSION_FACTOR_HEX)
        _remainders.append(number_to_string_hex(_temp_remainder))

    return '0x' + ''.join(str(num) for num in _remainders[::-1]) if _remainders else '0x0'


LOWER_LIMIT = 0
UPPER_LIMIT = 1_000_000_000

message_for_user = f'Please enter an integer between {LOWER_LIMIT} and {UPPER_LIMIT} -> '

number_from_user = user_input_number(message_for_user, LOWER_LIMIT, UPPER_LIMIT)

result = dec_to_hex(number_from_user)

print(f'Result       - {result}')
print(f'Result check - {hex(number_from_user)}')
