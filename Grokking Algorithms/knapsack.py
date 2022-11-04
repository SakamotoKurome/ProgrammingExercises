# 定义数据结构
class Good():
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight


goods = []
goods.append(Good('吉他', 1500, 1))
goods.append(Good('音响', 3000, 4))
goods.append(Good('笔记本电脑', 2000, 3))


# 背包问题的算法
def knapsack(goods, cap):
    table = [[0]*cap for _ in range(len(goods))]
    for i in range(len(goods)):
        for j in range(cap):
            if i == 0 and j+1 >= goods[i].weight:
                table[i][j] = goods[i].value
            else:
                if j+1 == goods[i].weight:
                    table[i][j] = max(table[i-1][j],
                                      goods[i].value)
                elif j+1 > goods[i].weight:
                    table[i][j] = max(table[i-1][j],
                                      goods[i].value +
                                      table[i-1][j-goods[i].weight])
                else:
                    table[i][j] = table[i-1][j]
    # 打印结果
    for row in table:
        for cell in row:
            print(cell, end=' ')
        print('\n')


knapsack(goods, 4)
