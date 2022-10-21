import random
secret = random.randint(1, 100)
guess = 0
tries = 0
print("我有一个秘密！")
print("是 1 之 99 的数字，你可以猜 6 次。")
while guess != secret and tries < 6:
    guess = int(input("你猜的数字："))
    if guess < secret:
        print("太小了")
    elif guess > secret:
        print("太大了")
    tries = tries + 1
if guess == secret:
    print("你猜对了！")
else:
    print("你可以猜的次数用完了。")
    print("正确答案是：", secret)
