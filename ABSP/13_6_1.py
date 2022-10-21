import os
import PyPDF2


def encrypt_pdf(password):
    # 遍历文件夹中的所有 PDF(包含子文件夹)
    base_dir = os.getcwd()
    for foldername, subfolders, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith('.pdf'):
                # 用命令行提供的口令对这些 PDF 加密
                file = os.path.join(foldername, filename)
                inputFileObj = open(file, 'rb')
                pdfReader = PyPDF2.PdfFileReader(inputFileObj)
                if not pdfReader.isEncrypted:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for i in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(i))
                    pdfWriter.encrypt(password)
                    # 用原来的文件名加上_encrypted.pdf后缀,保存每个加密的 PDF
                    encrypted_file = os.path.join(
                        foldername, f'{filename}_encrypted.pdf')
                    outputFileObj = open(encrypted_file, 'wb')
                    pdfWriter.write(outputFileObj)
                    inputFileObj.close()
                    outputFileObj.close()
                    # 删除原来的文件之前,尝试用一个程序读取并解密该文件,确保它被正确的加密
                    with open(encrypted_file, 'rb') as f:
                        pdfReader = PyPDF2.PdfFileReader(f)
                        if pdfReader.isEncrypted:
                            os.unlink(file)
                else:
                    inputFileObj.close()


# encrypt_pdf('rosebud')


def decrypt_pdf(password):
    # 找到文件夹中所有加密的 PDF 文件(包括它的子文件夹)
    base_dir = os.getcwd()
    for foldername, subfolders, filenames in os.walk(base_dir):
        for filename in filenames:
            if filename.endswith('.pdf'):
                file = os.path.join(foldername, filename)
                inputFileObj = open(file, 'rb')
                pdfReader = PyPDF2.PdfFileReader(inputFileObj)
                if pdfReader.isEncrypted:
                    # 利用提供的口令,创建 PDF 的解密拷贝。
                    try:
                        pdfReader.decrypt(password)
                        pdfWriter = PyPDF2.PdfFileWriter()
                        for i in range(pdfReader.numPages):
                            pdfWriter.addPage(pdfReader.getPage(i))
                        outputFileObj = open(os.path.join(
                            foldername, f'{filename}_decrypted.pdf'), 'wb')
                        pdfWriter.write(outputFileObj)
                        outputFileObj.close()
                    except:
                        # 如果口令不对,程序应该打印一条消息
                        print(f'Not Decrpted: {file}')
                        continue
                    else:
                        inputFileObj.close()
                else:
                    inputFileObj.close()
