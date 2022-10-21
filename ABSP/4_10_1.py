def format(string_list):
    result = ''
    for string in string_list[:-1]:
        result += string + ', '
    result += 'and ' + string_list[-1]
    return result


spam = ['apples', 'bananas', 'tofu', 'cats']
print(format(spam))
