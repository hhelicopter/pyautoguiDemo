import pyautogui

pyautogui.FAILSAFE = True # 保护措施，鼠标光标在屏幕左上角会产生FailSafeException异常。
pyautogui.PAUSE = 2.5 #函数增加延迟为2.5秒

def get_mouse_position():
    '''
    获取鼠标当前位置
    :return: 位置
    '''
    return pyautogui.position()

def get_img_position(img,confidence=0.9):
    '''
    匹配图像，获取图像位置
    :param img: 图像
    :param confidence: 匹配置信度
    :param grayscale: 灰度图匹配
    :return: 位置
    '''
    return pyautogui.locateCenterOnScreen(img, confidence=confidence,grayscale=True)

def shot_screen(path):
    '''
    截屏
    :param path: 图片存放路径
    :return: None
    '''
    pyautogui.screenshot(path)

def move_mouse(x,y,duration=0.2):
    '''
    移动鼠标到屏幕指定位置
    :param x: 横坐标
    :param y: 纵坐标
    :param duration: 延时
    :return: None
    '''
    pyautogui.moveTo(x, y, duration=0.2)

def move_mouse_rel(x,y,duration=0.2):
    '''
    移动鼠标到相对于光标当前所在位置
    :param x:横向偏移量
    :param y:横向偏移量
    :param duration:延时
    :return:None
    '''
    pyautogui.moveRel(x, y, duration=0.2)

def move_mouse_with_drag(x, y, time=2, button='left'):
    '''
    按下鼠标键同时移动到屏幕指定位置，
    :param x: 横坐标
    :param y: 纵坐标
    :param time: 点击时间
    :param button: 鼠标键位
    :return:None
    '''
    pyautogui.dragTo(x, y, time=time, button=button)

def mouse_click(clicks,button='left',interval=0.25):
    '''
    鼠标点击
    :param clicks: 点击次数
    :param button: 鼠标键位
    :param interval: 点击时间间隔
    :return:
    '''
    pyautogui.click(button=button, clicks=clicks, interval=interval)

def check_position_in_screen(x,y):
    '''
    检查坐标是否在屏幕内
    :param x: 横坐标
    :param y: 纵坐标
    :return: True/False
    '''
    return pyautogui.onScreen(0, 0)

def scroll(amount_to_scroll):
    '''
    窗口滚动
    :param amount_to_scroll:滚动的格数，正数向上、负数向下
    :return:
    '''
    pyautogui.scroll(clicks=amount_to_scroll)

def main():
    try:
        # print(get_mouse_position())
        # print(get_img_position("wechat.png"))
        # shot_screen()
        # move_mouse_rel(-100,100)
        # scroll(1000)
        mouse_click(1,'right')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()