import re


def password_chack(password):
    char_8 = re.compile(r'.{8,}', re.DOTALL)
    upper = re.compile(r'[a-z]+')
    lower = re.compile(r'[A-Z]+')
    number = re.compile(r'\d+')
    if char_8.search(password) == None or upper.search(password) == None or \
            lower.search(password) == None or number.search(password) == None:
        return False
    else:
        return True


def regex_strip(str1, str2=''):
    if not str2:
        start_end = re.compile(r'^\s+|\s+$')
    else:
        start_end = re.compile(f'^[{str2}]+|[{str2}]+$')
    return start_end.sub('', str1)
