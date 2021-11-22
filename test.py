import pyautogui

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
    :return:
    '''
    pyautogui.moveRel(x, y, duration=0.2)

def mouse_click():
    pass

def main():
    try:
        # print(get_mouse_position())
        # print(get_img_position("wechat.png"))
        # shot_screen()
        move_mouse_rel(-100,100)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()