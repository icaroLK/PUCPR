def convert_list_to_dict(l: list):
    d = {}
    for i, v in enumerate(l):
        d[i] = v
    return d

l = [32, 54, 76, 4235, 6543]
print(convert_list_to_dict(l))