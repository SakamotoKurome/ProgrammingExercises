tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def get_max_width(items):
    max_width = 0
    for item in items:
        width = len(item)
        if width > max_width:
            max_width = width
    return max_width


def printTable(tableData):
    col_widths = []
    for items in tableData:
        col_widths.append(get_max_width(items))
    cols = len(tableData)
    rows = len(tableData[0])
    for row in range(rows):
        for col in range(cols):
            print(tableData[col][row].rjust(col_widths[col]), end=' ')
        print()


printTable(tableData)
