def convert_list_to_dict(lista):
    dic = {}
    for c, v in enumerate(lista):
        dic[c] = v
    return dic






a = ['batata', 'morango', 'banana']

print(convert_list_to_dict(a))