import openpyxl
import os
# 一行一个单元格，一列一个文本文件
# 假定保存的txt在jobs目录
jobs_dir = os.path.join(os.getcwd(), 'jobs')
os.makedirs(jobs_dir, exist_ok=True)
wb = openpyxl.load_workbook('12_13_1.xlsx')
sheet = wb.active
for row in sheet:
    for cell in row:
        with open(os.path.join(jobs_dir, str(cell.column) + '.txt'), 'a') as f:
            if cell.value != None:
                f.write(str(cell.value)+'\n')
            else:
                f.write('\n')
