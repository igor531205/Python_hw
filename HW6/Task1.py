# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.​


from sys import argv as arg
from datetime import datetime as dt


def is_today(current_date: str, date: str) -> bool:

    return True if current_date == date else False


if __name__ == '__main__':

    _, *args = arg
    date = args.pop() if args else ''
    current_date = dt.now().date().strftime("%d.%m.%Y")

    message = f'Вы ввели сегодняшнюю дату {current_date}' if is_today(current_date, date) \
        else f'Вы ввели не корректную дату, сегодня {current_date}'

    print(message)
