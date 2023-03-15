import ctypes
import os
import psutil


def kill_task():
    for task in psutil.process_iter(['name']):
        if task.info['name'] == 'StudentMain.exe':
            pid = task.pid
            os.system(f'tskill {pid}')
            return True
    return False


if __name__ == '__main__':
    os.system(f'mode con cols=30 lines=10')
    print("#" * 30)
    print("一键关控 BY 雪中明月")
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("#" * 30)
        print('请以管理员权限运行！')
        print("#" * 30)
        input('回车以退出')
        exit()
    else:
        print("#" * 30)
        if kill_task():
            print('关掉了，好耶！')
        else:
            print('找不到进程了TAT')
        print("#" * 30)
        input('回车以退出')
        exit()
