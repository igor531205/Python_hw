# Напишите программу банкомат:
# - Начальная сумма равна нулю;
# - Допустимые действия: пополнить, снять, выйти;
# - Сумма пополнения и снятия кратны 50 у.е.;
# - Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.;
# - После каждой третей операции пополнения или снятия начисляются проценты - 3%;
# - Нельзя снять больше, чем на счёте;
# - При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной;
# - Любое действие выводит сумму денег.

from decimal import Decimal


class Atm():
    """Банкомат (automated teller machine)"""

    __MIN_WITHDRAWAL_COMMISSION__: Decimal = Decimal('30.00')
    __WITHDRAWAL_COMMISSION_PERCENT__: Decimal = Decimal('1.50')
    __MAX_WITHDRAWAL_COMMISSION__: Decimal = Decimal('600.00')
    __MULTIPLICITY__: Decimal = Decimal('50.00')

    def __init__(self):
        self.cash: Decimal = Decimal()

    def replenish(self):
        message_for_user = f'Enter the amount of ATM replenishment multiple {self.__MULTIPLICITY__} RUR -> '

    def withdraw(self):
        message_for_user = f'Enter the amount of withdrawal from the ATM multiple {self.__MULTIPLICITY__} RUR -> '

    def close(self):
        print(f'Your money: {self.cash} RUR')
        exit()


def show_menu() -> int:
    """Меню выбора действия.
    :return: Значение выбранного действия.
    """
    MIN_CHOICE = 0
    MAX_CHOICE = 2
    MESSAGE_FOR_USER = (f''' {'"'*10} Main menu: {'"'*10}
                        \r {REPLENISH}. "Replenish cash an ATM"
                        \r {WITHDRAW}. "Withdraw cash an ATM"
                        \r 0. "Close the ATM"
                        \r Enter menu item number -> ''')
    return user_input_number(MESSAGE_FOR_USER, MIN_CHOICE, MAX_CHOICE)


def user_input_number(message: str, lower_limit: int = 0, upper_limit: int = 5_000_000) -> int:
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

                print()
                return _number
        print('You entered an invalid value\n')


REPLENISH: int = 1
WITHDRAW: int = 2

atm = Atm()

while True:

    choice: int = show_menu()

    if choice == REPLENISH:
        atm.replenish()

    elif choice == WITHDRAW:
        atm.withdraw()

    else:
        atm.close()
