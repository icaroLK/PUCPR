def divide_dict(dic):
    chaves = list(dic.keys())
    valores = list(dic.values())
    tupla = (chaves, valores)
    return tupla



a = {"primeiro": 'batata', 'segundo': 'morango', 'terc': 'penis'}

print(divide_dict(a))