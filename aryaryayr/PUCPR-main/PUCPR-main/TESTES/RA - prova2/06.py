def divide_dict(d: dict):
    keys = list(d.keys())
    values = list(d.values())
    tuple = (keys, values)
    return tuple


d = {'Ary': 18, 'Adriano': 18, 'Maircris': 30, 'Ícaro': 17}

print(divide_dict(d))