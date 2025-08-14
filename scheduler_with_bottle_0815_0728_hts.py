# 代码生成时间: 2025-08-15 07:28:12
import bottle
from bottle import route, run, template
import datetime
import threading
import schedule
import time

# 定时任务调度器类
class Scheduler:
    def __init__(self):
        self.jobs = []

    def add_job(self, job_func, interval):
        """添加定时任务"""
        self.jobs.append((job_func, interval))
        schedule.every(interval).seconds.do(job_func)

    def run(self):
        """运行所有定时任务"""
        while True:
            schedule.run_pending()
            time.sleep(1)

# Bottle 路由和视图函数
@route('/')
def index():
    return template('index')  # 假设有一个名为“index”的模板文件

# 定时执行的任务函数
def timed_task():
    print("定时任务执行: {}".format(datetime.datetime.now()))

# Bottle 应用实例
app = bottle.default_app()

# 创建定时任务调度器实例
scheduler = Scheduler()

# 添加定时任务
scheduler.add_job(timed_task, 10)  # 每10秒执行一次

# 启动定时任务调度器线程
threading.Thread(target=scheduler.run, daemon=True).start()

# 运行 Bottle 应用
run(app, host='localhost', port=8080)
