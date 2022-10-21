import easygui
F = float(easygui.enterbox("输入华氏度："))
C = 5 / 9 * (F - 32)
easygui.msgbox("对应摄氏度为："+str(C))
m1 = easygui.enterbox("姓名", default="John Snead")
m2 = easygui.enterbox("房间号、街道和城市", default="28 Main Street")
m3 = easygui.enterbox("省 / 地区 / 州", default="Akron, Ohio")
m4 = easygui.enterbox("邮政编码", default="12345")
easygui.msgbox(f"{m1}\n{m2}\n{m3}\n{m4}")
