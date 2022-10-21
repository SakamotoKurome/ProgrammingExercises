info_names = ["名字：", "地址：", "街道：", "城市：", "州或省：", "邮政编码：", "国家："]


def print_info(info):
    print("你的信息如下")
    for i in range(7):
        print(info_names[i]+info[i])


info = []
for name in info_names:
    info.append(input("请输入"+name))
print_info(info)
