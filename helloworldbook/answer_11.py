import time
seconds = int(input("你想从哪里开始计数："))
for i in range(seconds, 0, -1):
    print(i, end=" ")
    for j in range(i):
        print('*', end=" ")
    print()
    time.sleep(1)
print("结束！")
