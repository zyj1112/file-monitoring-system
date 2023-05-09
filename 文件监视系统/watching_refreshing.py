import sys
import time
from watchdog.observers import Observer # 监控
from watchdog.events import * # 触发事件
from selenium import  webdriver
"""
watchdog 提供了指定目录/文件的变化监控，对于指定目录内的操作，被视为一次事件。
如添加删除文件或目录、重命名文件或目录、修改文件内容等，每种变化都会触发一次事件，事件是用户定义的业务逻辑代码。
"""
class FileEventHandler(FileSystemEventHandler): # 继承一些库中的类

    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        if event.is_directory: # 如果该事件由一个目录触发（通俗些说就是文件夹）
            print(f"{now} Directory was moved from {event.src_path} to {event.dest_path}")
        else:
            print(f"{now} File was moved from {event.src_path} to {event.dest_path}")

    def on_created(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:  # 如果该事件由一个目录触发（通俗些说就是文件夹）
            print(f"{now} Directory  {event.src_path} was created")
        else: # 如果该事件由一个文件触发
            print(f"{now} File  {event.src_path} was created")

    def on_deleted(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:  # 如果该事件由一个目录触发（通俗些说就是文件夹）
            print(f"{now} Directory  {event.src_path} was deleted")
        else:
            print(f"{now} File  {event.src_path} was deleted")

    def on_modified(self, event):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        if event.is_directory:  # 如果该事件由一个目录触发（通俗些说就是文件夹）
            print(f"{now} Directory  {event.src_path} was modified")
        else:
            print(f"{now} File  {event.src_path} was modified")
        return True

if __name__ == "__main__" :

    observer = Observer()
    path = "d://testt"
    event_handler = FileEventHandler()
    observer.schedule(event_handler, path, True)
    print(f"Start monitor directory {path}")
    driver = webdriver.Chrome() # Chrome浏览器驱动
    driver.get("file:///C:/Users/Lenovo/Desktop/chickenglass/output/example.html")
    observer.start() # 创建一个新线程
    try:
        while True:
            driver.refresh()
            time.sleep(1) # 保持主线程运行 一秒一次监视
    except KeyboardInterrupt:
        observer.stop() # 线程结束前做一些工作

    observer.join() # 结束线程