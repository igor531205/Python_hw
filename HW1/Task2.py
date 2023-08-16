# Напишите код, который запрашивает число и сообщает является ли оно простым
# или составным. Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя». Сделайте ограничение на
# ввод отрицательных чисел и чисел больше 100 тысяч.


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


def prime_number_test(number: int) -> str:
    """Проверка на простое число.
    :param number: Число для проверки.    
    :return: Результат проверки.
    """

    if number == 1 or number == 2:
        return f'Prime number'

    elif number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return f'Prime number'

        return f'Composite number'

    else:
        return f'Not prime number and not composite number'


LOWER_LIMIT = 0
UPPER_LIMIT = 100000

message_for_user = f'Please enter a natural number from '\
                   + f'{LOWER_LIMIT} to {UPPER_LIMIT} -> '

number_from_user = user_input_number(
    message_for_user, LOWER_LIMIT, UPPER_LIMIT)

result = prime_number_test(number_from_user)

print(f'{result} - {number_from_user}')
