import time

import keyboard
import pyautogui

import unit

# 全局退出标志
exit_flag = False

def trigger():
    """
    触发程序
    :return:None
    """
    while True:
        if exit_flag:
            exit()
        pyautogui.screenshot().save('./jietu/screenshot1.png')
        if unit.is_img_exist('./jietu/screenshot1.png', './img/2.jpeg'):
            # 判断是否选择技能
            for i in range(5):
                unit.my_click(971, 549)
                unit.my_click(957, 995)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/3.jpeg'):
            # 判断是否出现惊喜奖励
            unit.my_click(951, 890)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/4.jpeg'):
            # 判断一次异星守护是否结束
            unit.my_click(978, 972)
            time.sleep(3)
            # 查看积分
            unit.my_click(115, 990)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/5.jpeg'):
            # 分数已达上限，退出脚本
            pyautogui.screenshot(region=[149, 976, 106, 35]).save('./jietu/screenshot2.png')
            if int(unit.my_ocr('../jietu/screenshot2.png')) >= 70000:
                # 可选是否退出游戏，游戏进程为'Game.exe'，若出现同名进程，存在误删可能
                # unit.kill_process_by_name('Game.exe')
                exit()
            unit.my_click(1801, 50)
            time.sleep(3)
        elif unit.is_img_exist('./jietu/screenshot1.png', './img/1.jpeg'):
            # 开启下一轮异星守护
            unit.my_click(1706, 989)

def on_key(event):
    # 声明一个全局变量，用于判断是否退出程序
    global exit_flag
    # 如果按下的键是F8键
    if event.name == 'f8':
        # 将全局变量exit_flag设置为True
        exit_flag = True
        # 打印提示信息
        print("F8 key pressed, exiting program...")
        # 退出程序
        exit()


keyboard.on_press(on_key)
try:
    unit.bring_to_front('尘白禁区')
except Exception as e:
    print(e)
    exit()
trigger()

