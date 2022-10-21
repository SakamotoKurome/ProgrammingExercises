import time
import random
random_list = []
for i in range(5):
    random_list.append(random.randint(1, 20))
print(random_list)
for i in range(10):
    print(random.random())
    time.sleep(3)
