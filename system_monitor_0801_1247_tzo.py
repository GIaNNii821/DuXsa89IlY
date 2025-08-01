# 代码生成时间: 2025-08-01 12:47:51
from bottle import route, run, template
import psutil
import platform

# 获取系统信息的函数
def get_system_info():
    system_info = {}
    system_info['platform'] = platform.system()
    system_info['cpu_cores'] = psutil.cpu_count(logical=False)
    system_info['cpu_usage'] = psutil.cpu_percent(interval=1)
    system_info['memory_total'] = psutil.virtual_memory().total
    system_info['memory_available'] = psutil.virtual_memory().available
    system_info['disk_partitions'] = psutil.disk_partitions()
    return system_info

# Bottle路由定义
@route('/')
def monitor():
    try:
        info = get_system_info()
        return template('monitor_template', info=info)
    except Exception as e:
        return {'error': str(e)}

# 启动Bottle服务器
if __name__ == '__main__':
    run(host='localhost', port=8080)

# 以下是HTML模板，用于显示系统性能监控信息
monitor_template = """
<!DOCTYPE html>
<html>
<head>
    <title>System Monitor</title>
</head>
<body>
    <h1>System Information</h1>
    <p>Platform: {{info.platform}}</p>
    <p>CPU Cores: {{info.cpu_cores}}</p>
    <p>CPU Usage: {{info.cpu_usage}}%</p>
    <p>Total Memory: {{info.memory_total}} MB</p>
    <p>Available Memory: {{info.memory_available}} MB</p>
    <h2>Disk Partitions</h2>
    <ul>
        %for partition in info.disk_partitions:
        <li>{{partition.device}} - {{partition.mountpoint}} - {{partition.fstype}} ({{partition.opts}})</li>
        %end
    </ul>
</body>
</html>
"""