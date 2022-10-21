import PyPDF2
from PyPDF2 import PasswordType
# 读取文件
with open('dictionary.txt') as f:
    # 创建一个单词字符串的列表
    words = f.readlines()
f_obj = open('encrypted.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(f_obj)
# 循环遍历这个列表中的每个单词,将它传递给 decrypt()方法
for word in words:
    # 应该尝试每个单词的大小写形式
    if not pdf_reader.decrypt(word.upper()) == PasswordType.NOT_DECRYPTED \
            or not pdf_reader.decrypt(word.lower()) == PasswordType.NOT_DECRYPTED:
        print(f'Password: {word}')
f_obj.close()
