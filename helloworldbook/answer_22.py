import random
import pickle
words = []
words_file = open('answer_22_words.txt', 'r')
lines = words_file.readlines()
words_file.close()
for line in lines:
    words.append(line.strip().split(','))
print("The" + random.choice(words[0]) + random.choice(words[1]) +
      random.choice(words[2]) + random.choice(words[3]))
# for i in ['名字', '年龄', '最喜欢的颜色', '最喜欢的食物']:
#     file_obj = open('answer_22_'+i+'.txt', 'w')
#     file_obj.write(input('请输入你'+i+'：'))
#     file_obj.close()
info = []
for i in ['名字', '年龄', '最喜欢的颜色', '最喜欢的食物']:
    info.append(input('请输入你'+i+'：'))
file_obj = open('answer_22_info.pkl', 'wb')
pickle.dump(info, file_obj)
file_obj.close()
