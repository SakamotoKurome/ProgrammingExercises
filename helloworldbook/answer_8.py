table = int(input("你要显示哪个乘法表？"))
max = int(input("最大乘到几？"))
for i in range(1, max+1):
    print(f"{table} x {i} = {table * i}")
j = 1
while j < 11:
    print(f"{table} x {j} = {table * j}")
    j = j + 1
