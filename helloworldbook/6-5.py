import random
import easygui
secret = random.randint(1, 100)
guess = 0
tries = 0
easygui.msgbox("我有一个秘密！"+"是 1 之 99 的数字，你可以猜 6 次。")
while guess != secret and tries < 6:
    guess = easygui.integerbox("你猜的数字：")
    if guess < secret:
        easygui.msgbox("太小了")
    elif guess > secret:
        easygui.msgbox("太大了")
    tries = tries + 1
if guess == secret:
    easygui.msgbox("你猜对了！")
else:
    easygui.msgbox("你可以猜的次数用完了！你失败了，真是糟糕呢。")
    easygui.msgbox("正确答案是："+str(secret))
