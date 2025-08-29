# 代码生成时间: 2025-08-29 12:53:13
from bottle import route, run, request, response
import json
import os
import shutil
import datetime
import tarfile

# 配置文件和备份目录路径
BACKUP_DIR = 'backups'

# 检查备份目录是否存在，如果不存在则创建
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)

# 备份数据
@route('/backup', method='GET')
def backup_data():
    try:
        # 生成备份文件名
        timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        backup_filename = f'backup_{timestamp}.tar.gz'
        backup_path = os.path.join(BACKUP_DIR, backup_filename)

        # 选择需要备份的文件夹或文件
        with tarfile.open(backup_path, "w:gz") as tar:
            tar.add('data', arcname='data')

        # 返回备份成功的信息
        response.status = 200
        return json.dumps({'message': f'Backup created successfully: {backup_filename}'})
    except Exception as e:
        response.status = 500
        return json.dumps({'error': str(e)})

# 恢复数据
@route('/restore', method='POST')
def restore_data():
    try:
        # 获取上传的文件
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            response.status = 400
            return json.dumps({'error': 'No file uploaded'})

        # 保存上传的文件到备份目录
        backup_path = os.path.join(BACKUP_DIR, uploaded_file.filename)
        with open(backup_path, 'wb') as f:
            f.write(uploaded_file.file.read())

        # 解压备份文件
        with tarfile.open(backup_path, "r:gz") as tar:
            tar.extractall(path='data')

        # 返回恢复成功的信息
        response.status = 200
        return json.dumps({'message': 'Restore completed successfully'})
    except Exception as e:
        response.status = 500
        return json.dumps({'error': str(e)})

# 运行服务
if __name__ == '__main__':
    run(host='localhost', port=8080)