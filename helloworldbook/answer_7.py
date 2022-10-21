cost = float(input("购买的价格？"))
if cost <= 10:
    print("给你 10% 的折扣")
    cost = cost * (1-0.1)
elif cost > 10:
    print("给你 20% 的折扣")
    cost = cost * (1-0.2)
print("最终价格为：", cost)
sex = input("你的性别(m/f)：")
old = int(input("你的年龄："))
if sex == "f" and 10 <= old <= 12:
    print("你可以加入球队")
else:
    print("抱歉，你不适合")
size_tank = int(input("你的油箱有多大(单位是升)?"))
percent_full = int(input("油箱有多满(按百分比,例如,半满就是 50%)? "))
km_liter = int(input("你的汽车每升油可以走多远(km)?"))
print("你的油箱大小：", size_tank)
print("油箱有多满：", percent_full)
print("每升油可走：", km_liter)
can_go = size_tank * (percent_full / 100) * km_liter
print("你还可以走", can_go, "km")
print("下一个加油站有200km")
if can_go > 200:
    print("你可以等到下一站再加油")
else:
    print("立刻加油！")
password = input("输入密码：")
if password == "right":
    print("登陆成功！")
else:
    print("登陆失败！")
