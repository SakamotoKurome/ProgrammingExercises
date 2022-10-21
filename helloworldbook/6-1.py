import easygui
flavor = easygui.buttonbox(
    "你喜欢什么动物？", choices=['猫是最好的', '狗狗最好了', "我最害怕蛇了", "我想要一只熊"])
flavor = easygui.choicebox(
    "你喜欢什么动物？", choices=['猫是最好的', '狗狗最好了', "我最害怕蛇了", "我想要一只熊"])
flavor = easygui.enterbox(
    "What is your favorite ice cream flavor?", default="Goodbye")
easygui.msgbox("这是你奇奇怪怪的选择：" + flavor)
