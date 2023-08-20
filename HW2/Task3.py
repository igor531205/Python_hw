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

    _ZERRO_RUR: Decimal = Decimal('0.00')
    _MULTIPLICITY_RUR: Decimal = Decimal('50.00')
    _MIN_WITHDRAWAL_COMMISSION_RUR: Decimal = Decimal('30.00')
    _MAX_WITHDRAWAL_COMMISSION_RUR: Decimal = Decimal('600.00')
    _WEALTH_RUR: Decimal = Decimal('5_000_000.00')

    _REMUNERATION_COUNT: Decimal = Decimal('3')

    _FULL_PERCENT: Decimal = Decimal('100')
    _WITHDRAWAL_COMMISSION_PERCENT: Decimal = Decimal('1.5')
    _REMUNERATION_PERCENT: Decimal = Decimal('3')
    _WEALTH_PERCENT: Decimal = Decimal('10')

    def __init__(self):
        self._cash: Decimal = Decimal(self._ZERRO_RUR)

    def _balance(self):
        """Вывод суммы остатка средств (баланс).        
        """
        print(f'Your money: {self._cash} RUR\n')

    def _user_input_decimal(self, message: str) -> Decimal:
        """Пользовательский ввод суммы операции.
        :param message: Сообщение пользователю.
        :return: Сумма операции.
        """

        while True:

            _string = input(f'{message}').replace(',', '.')

            _decimal_args = _string.split('.')

            _COUNT_OF_ARGUMENTS_DECIMAL = 2

            if len(_decimal_args) <= _COUNT_OF_ARGUMENTS_DECIMAL and all(a.isdigit() for a in _decimal_args):

                _decimal = Decimal(_string)
                if _decimal > 0 and not _decimal % self._MULTIPLICITY_RUR:
                    return _decimal
                else:
                    print(f'Cancel operation.')

            else:
                print('You entered the amount in the wrong format!')

    def replenish(self):
        """Операция пополнения.        
        """
        message_for_user = (f''' Enter the amount of ATM replenishment multiple {self._MULTIPLICITY_RUR} RUR -> ''')

        self._cash += self._user_input_decimal(message_for_user)

        self._balance()

    def withdraw(self):
        """Операция снятия.        
        """
        message_for_user = (f''' Withdrawal commision of ATM replenishment - {self._WITHDRAWAL_COMMISSION_PERCENT}%.
                           \r Minimum commission - {self._MIN_WITHDRAWAL_COMMISSION_RUR} RUR. 
                           \r Maximum commission - {self._MAX_WITHDRAWAL_COMMISSION_RUR} RUR.
                           \r Enter the amount of withdrawal from the ATM multiple {self._MULTIPLICITY_RUR} RUR -> ''')

        _request = self._user_input_decimal(message_for_user)
        _operation_commission = _request * self._WITHDRAWAL_COMMISSION_PERCENT / self._FULL_PERCENT

        if _operation_commission < self._MIN_WITHDRAWAL_COMMISSION_RUR:
            _operation_commission = self._MIN_WITHDRAWAL_COMMISSION_RUR

        elif _operation_commission > self._MAX_WITHDRAWAL_COMMISSION_RUR:
            _operation_commission = self._MAX_WITHDRAWAL_COMMISSION_RUR

        _request_sum = _request + _operation_commission

        if _request_sum <= self._cash:
            self._cash -= _request_sum

        else:
            print(f'Cancel operation - Insufficient funds on the account')

        self._balance()

    def close(self):
        """Выйти.        
        """
        self._balance()
        exit()


def show_menu() -> int:
    """Меню выбора действия.
    :return: Значение выбранного действия.
    """

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

                    print()
                    return _number
            print('You entered an invalid value\n')

    MIN_CHOICE = 0
    MAX_CHOICE = 2
    MESSAGE_FOR_USER = (f''' {'"'*10} Main menu: {'"'*10}
                        \r {REPLENISH}. "Replenish cash an ATM"
                        \r {WITHDRAW}. "Withdraw cash an ATM"
                        \r 0. "Close the ATM"
                        \r Enter menu item number -> ''')
    return user_input_number(MESSAGE_FOR_USER, MIN_CHOICE, MAX_CHOICE)


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
