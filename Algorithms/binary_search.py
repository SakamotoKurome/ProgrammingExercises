import sys


# 二分查找算法
def binary_search(key, a):
    lo = 0
    hi = len(a) - 1
    while (lo <= hi):
        mid = lo + (hi - lo) / 2
        mid = int(mid)
        if key < a[mid]:
            hi = mid - 1
        elif key > a[mid]:
            lo = mid + 1
        else:
            return mid
    return -1


# 读取从命令行获取的文件名
whitelist = []
f_obj = open(sys.argv[1])
for line in f_obj:
    whitelist.append(int(line))
f_obj.close()
# 从小到大排序
whitelist.sort()
# 在有序列表中查找命令行余下的数字
for i in range(2, len(sys.argv)):
    key = int(sys.argv[i])
    if binary_search(key, whitelist) == -1:
        print(key)
