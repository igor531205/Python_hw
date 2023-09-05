# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.


def key_parameters_to_dictionary(**kwargs):
    """Функция перевода ключевых параметров в словарь."""

    new_dict = {}
    for key, value in kwargs.items():

        new_dict[hash(value) if hash(value) == value else str(value)] = key

    return new_dict


print(key_parameters_to_dictionary(course='python', homework=4, task=2))
