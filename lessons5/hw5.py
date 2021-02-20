import re


def normalize(string):
    global d
    my_set = string.maketrans("абвгдеёжзийклмнопрстуфхцчшщъыьэюя",
                              "abvgdeëžzijklmnoprstufhcčššъyьèûâ")
    my_list = []
    
    for el in string:
        if el == el.lower():
            d = el.translate(my_set)
        elif el == el.upper():
            d = el.lower().translate(my_set).upper()
        my_list.append(d)
        
    k = re.sub(r'(\W)', '_', ''.join(my_list))
    return k

string = input("Введите строку: ")

print(normalize(string))

