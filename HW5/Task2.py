# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25 %».
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.


def calculating_bonus(_names, _salaries, _awards) -> dict:
    """Функция транспонирования абсолютного пути до файла в кортеж из трёх элементов."""

    ONE_HUNDRED_PERCENT = 100

    return {name: salary * float(award[:-1]) / ONE_HUNDRED_PERCENT
            for name, salary, award in zip(_names, _salaries, _awards)}


names = ['Andrey', 'Marina', 'Fedor']
salaries = [80_000, 200_000, 150_000]
awards = ['10.25%', '5.50%', '15.75%']


print(calculating_bonus(names, salaries, awards))
