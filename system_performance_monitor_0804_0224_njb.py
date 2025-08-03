# 代码生成时间: 2025-08-04 02:24:39
# system_performance_monitor.py

# 导入必要的库
from bottle import route, run, template
import psutil
import platform
import subprocess

# 定义全局变量，用于存储系统信息
info = {"cpu": None, "memory": None, "disk": None, "network": None}

# 函数：获取CPU使用率
def get_cpu_usage():
    with open("/proc/cpuinfo") as f:
        cpu_info = f.read()
    # 提取CPU信息并计算使用率
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage

# 函数：获取内存使用情况
def get_memory_usage():
    memory = psutil.virtual_memory()
    return {"total": memory.total, "used": memory.used, "available": memory.available, "percent": memory.percent}

# 函数：获取磁盘使用情况
def get_disk_usage():
    partitions = psutil.disk_partitions()
    disk_usage = {}
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage[partition.device] = {"total": usage.total, "used": usage.used, "free": usage.free, "percent": usage.percent}
    return disk_usage

# 函数：获取网络使用情况
def get_network_usage():
    network_stats = psutil.net_io_counters(pernic=True)
    network_usage = {}
    for interface, stats in network_stats.items():
        network_usage[interface] = {"sent": stats.bytes_sent, "received": stats.bytes_recv}
    return network_usage

# Bottle路由：获取系统性能信息
@route("/performance")
def system_performance():
    try:
        info["cpu"] = get_cpu_usage()
        info["memory"] = get_memory_usage()
        info["disk"] = get_disk_usage()
        info["network"] = get_network_usage()
    except Exception as e:
        return template("error.tpl", error=str(e))
    return template("performance.tpl", info=info)

# Bottle路由：获取系统信息
@route("/info")
def system_info():
    info["os"] = platform.system()
    info["os_version"] = platform.release()
    info["hostname"] = platform.node()
    return template("info.tpl", info=info)

# 运行Bottle应用
if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)