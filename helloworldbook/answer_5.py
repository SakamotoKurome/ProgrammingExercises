firstName = "名"
lastName = "姓"
print(firstName, lastName)
firstName = input("名：")
lastName = input("姓：")
print(firstName, lastName)
length = float(input("你房子有多长？"))
width = float(input("你房子有多宽？"))
price = float(input("每平方尺的地毯要多少钱？"))
area_feet = length * width
area_yards = area_feet / 9
print("需要", area_feet, "平方米的地毯")
print("也就是", area_yards, "平方尺的地毯")
print("总共需要", area_yards * price, "元")
五分币 = int(input("有多少个五分币?"))
二分币 = int(input("有多少个二分币?"))
一分币 = int(input("有多少个一分币?"))
print("总共有零钱", 五分币*5 + 二分币*2 + 一分币, "分")
