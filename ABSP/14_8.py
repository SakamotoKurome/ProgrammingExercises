import os
import openpyxl
import csv
# 读取当前工作目录中的所有 Excel 文件
for filename in os.listdir(os.getcwd()):
    if filename.endswith('.xlsx'):
        wb = openpyxl.load_workbook(filename)
        for sheetname in wb.sheetnames:
            # 为每个表创建一个 CSV 文件。<Excel 文件名>_<表标题>.csv
            csv_filename = f'{filename[:-5]}_{sheetname}.csv'
            csv_file_obj = open(csv_filename, 'w')
            csv_writer = csv.writer(csv_file_obj)
            # 读取每个表，每个表的每一行
            sheet = wb[sheetname]
            for row in sheet:
                row_data = []
                for cell in row:
                    row_data.append(cell.value)
                csv_writer.writerow(row_data)
            csv_file_obj.close()
