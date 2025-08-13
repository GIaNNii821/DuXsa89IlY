# 代码生成时间: 2025-08-13 20:39:40
import os
from bottle import route, run, request, response
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from pandas import DataFrame
import numpy as np

# Bottle路由配置
@route('/generate_excel', method='POST')
def generate_excel():
    # 获取上传的文件
    uploaded_file = request.files.get('file')
    if not uploaded_file:
        return {'error': 'No file provided'}

    # 保存上传的文件
    temp_file_path = 'temp_upload.csv'
    with open(temp_file_path, 'wb') as f:
        f.write(uploaded_file.file.read())

    # 读取CSV文件并生成Excel
    try:
        df = DataFrame(np.genfromtxt(temp_file_path, delimiter=',', encoding='utf-8'))
        wb = Workbook()
        ws = wb.active
        for r_idx, row in enumerate(dataframe_to_rows(df, index=False, header=True), 1):
            for c_idx, value in enumerate(row, 1):
                ws.cell(row=r_idx, column=c_idx, value=value)

        # 保存工作簿
        excel_file_path = 'generated_excel.xlsx'
        wb.save(excel_file_path)

        # 设置响应头，以便于浏览器识别文件
        response.content_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        with open(excel_file_path, 'rb') as f:
            return f.read()
    except Exception as e:
        return {'error': 'Failed to generate Excel', 'details': str(e)}
    finally:
        # 清理临时文件
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        if os.path.exists(excel_file_path):
            os.remove(excel_file_path)

# 运行Bottle应用
run(host='localhost', port=8080, debug=True)
