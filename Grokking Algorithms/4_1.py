import numbers


def sum(arry):
    # 基线条件
    if arry == []:
        return 0
    else:
        # 递归条件指
        total = arry[0]+sum(arry[1:])
        return total


def item_number(arry):
    if arry == []:
        return 0
    else:
        number = 1 + item_number(arry[1:])
        return number


def max_number(arry):
    if arry == []:
        return 0
    else:
        a = arry[0]
        b = max_number(arry[1:])
        if a > b:
            return a
        else:
            return b


print(max_number([1, 2, 3]))
