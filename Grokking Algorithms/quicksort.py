def quicksort(arry):
    if len(arry) < 2:
        return arry
    else:
        pivot = arry[0]  # 基准值
        left = []  # 小于基准值的元素
        right = []  # 大于基准值的元素
        for item in arry[1:]:
            if item > pivot:
                left.append(item)
            else:
                right.append(item)
        return quicksort(right) + [pivot] + quicksort(left)


print(quicksort([1, 3, 2, 8, 7, 5, 6]))
