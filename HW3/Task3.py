# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.


def pack_backpack(_items: dict[str, int], _max_weight: int) -> list[int]:

    _possible_items = []

    for _item, _weight in _items.items():

        if _weight <= _max_weight:

            _possible_items.append(_item)
            _max_weight -= _weight

    return _possible_items


MAX_WEIGHT = 11
items = {'water': 5, 'food': 3, 'matches': 1, 'tent': 10, 'fleabag': 2}

print(pack_backpack(items, MAX_WEIGHT))
