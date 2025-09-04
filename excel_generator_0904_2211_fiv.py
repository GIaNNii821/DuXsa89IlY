# 代码生成时间: 2025-09-04 22:11:38
# excel_generator.py

"""
Excel表格自动生成器，使用PYTHON和BOTTLE框架。
"""

import bottle
import xlsxwriter
from datetime import datetime
import os
import sys

# 配置Bottle
bottle.TEMPLATE_PATH.insert(0, './views')

def create_excel_file(rows, cols, filename):
    """
    创建一个Excel文件
    :param rows: 行数
    :param cols: 列数
    :param filename: 文件名
    :return: 文件路径
    """
    try:
        with xlsxwriter.Workbook(filename) as workbook:
            worksheet = workbook.add_worksheet()

            for row in range(rows):
                for col in range(cols):
                    worksheet.write(row, col, f'Cell {row+1},{col+1}')
        return f'{os.path.abspath(filename)}'
    except Exception as e:
        print(f'Error creating Excel file: {e}')
        return None


def excel_route():
    """
    创建Excel文件的路由函数
    """
    rows = int(bottle.request.forms.get('rows', 10))
    cols = int(bottle.request.forms.get('cols', 10))
    filename = f'{datetime.now().strftime("%Y%m%d%H%M%S")}_{bottle.request.forms.get(