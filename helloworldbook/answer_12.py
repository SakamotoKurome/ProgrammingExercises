print("添加五个名字")
names = []
for i in range(5):
    names.append(input("添加第 " + str(i+1) + " 个名字："))
print("你输入了这些名字：", end="")
for name in names:
    print(name, end=" ")
print()
names_sorted = sorted(names)
print("你输入了这些名字(排序后）：", end="")
for name in names_sorted:
    print(name, end=" ")
print()
print("第三个名字是：", names[2])
name_new_index = int(input("你想替换那个名字？（1-5）："))
name_new = input("新名字：")
names[name_new_index-1] = name_new
print("这是修改后的名字：", end="")
for name in names:
    print(name, end=" ")
print()
