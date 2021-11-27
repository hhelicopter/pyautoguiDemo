import pyautogui
import time
import random

pyautogui.FAILSAFE = True # 保护措施，鼠标光标在屏幕左上角会产生FailSafeException异常。
# pyautogui.PAUSE = 2.5 #函数增加延迟为2.5秒

class Base:
    '''
    封装pyautogui方法的基础类
    '''
    def _get_mouse_position(self):
        '''
        获取鼠标当前位置
        :return: 位置
        '''
        return pyautogui.position()

    def _get_img_position(self,img,_confidence=0.9,_grayscale=True):
        '''
        匹配图像，获取图像位置
        :param img: 图像
        :param _confidence: 匹配置信度
        :param _grayscale: 灰度图匹配
        :return: 位置
        '''
        return pyautogui.locateCenterOnScreen(img, confidence=_confidence,grayscale=_grayscale)

    def _shot_screen(path):
        '''
        截屏
        :param path: 图片存放路径
        :return: None
        '''
        pyautogui.screenshot(path)

    def _move_mouse(self, x,y,_duration=0.2):
        '''
        移动鼠标到屏幕指定位置
        :param x: 横坐标
        :param y: 纵坐标
        :param _duration: 延时
        :return: None
        '''
        pyautogui.moveTo(x, y, duration=_duration)

    def _move_mouse_rel(self,x,y,_duration=0.2):
        '''
        移动鼠标到相对于光标当前所在位置
        :param x:横向偏移量
        :param y:横向偏移量
        :param _duration:延时
        :return:None
        '''
        pyautogui.moveRel(x, y, duration=_duration)

    def _move_mouse_with_drag(self, x, y, time=2, _button='left'):
        '''
        按下鼠标键同时移动到屏幕指定位置，
        :param x: 横坐标
        :param y: 纵坐标
        :param time: 点击时间
        :param _button: 鼠标键位
        :return:None
        '''
        pyautogui.dragTo(x, y, time=time, button=_button)

    def _mouse_click(self,clicks,button='left',_interval=0.25):
        '''
        鼠标点击
        :param clicks: 点击次数
        :param button: 鼠标键位
        :param interval: 点击时间间隔
        :return:
        '''
        pyautogui.click(button=button, clicks=clicks, interval=_interval)

    def _check_position_in_screen(self,x,y):
        '''
        检查坐标是否在屏幕内
        :param x: 横坐标
        :param y: 纵坐标
        :return: True/False
        '''
        return pyautogui.onScreen(x, y)

    def _scroll(self,amount_to_scroll):
        '''
        窗口滚动
        :param amount_to_scroll:滚动的格数，正数向上、负数向下
        :return:
        '''
        pyautogui.scroll(clicks=amount_to_scroll)


class App(Base):
    '''
    应用类
    '''
    def find_img_left_mouse_click(self,path,click=1):
        position = self._get_img_position(path)
        if position:
            self._move_mouse(position[0],position[1])
            self._mouse_click(click)
            time.sleep(3)
            return True
        else:
            print("not found")
            return False

    def find_img_move_mouse_rel_click_once(self,path,x_rel,y_rel):
        position = self._get_img_position(path)
        if position:
            self._move_mouse(position[0],position[1])
            self._move_mouse_rel(x_rel, y_rel) #75 110 145
            self._mouse_click(1)
            time.sleep(3)
            return True
        else:
            print("not found")
            return False

    def scroll_up_down(self):
        self._scroll(-1200)
        time.sleep(12)
        self._scroll(1200)
        time.sleep(12)

        self._scroll(-1200)
        time.sleep(12)
        self._scroll(1200)
        time.sleep(12)

    def close_page(self):
        '''
        关闭页面
        :return:
        '''
        with pyautogui.hold('ctrl'):
            pyautogui.press(['w'])
        time.sleep(3)

    def down_page_use_sapce(self):
        pyautogui.press(['space'])
        time.sleep(3)

    def scroll_page_find_img(self,roll,img):
        index = 0
        while not self._get_img_position(img):
            self._scroll(roll)
            time.sleep(1)
            index += 1
            if index == 6:
                return False
        return True



def main():
        app = App()
        # 阅读文章
        app.find_img_left_mouse_click("./img/homepage.png")
        time.sleep(3)
        app.find_img_left_mouse_click("./img/toutiao.png")
        time.sleep(3)
        rand_num = random.randint(1, 15)
        app.down_page_use_sapce()
        # 切换页面
        for i in range(rand_num):
            app.find_img_left_mouse_click("./img/pagepass.png")
        app.find_img_left_mouse_click("./img/toutiao.png")
        page_list = [-75,-110,-145,-180,-215,-250,75,110,145,180,215,250]
        random.shuffle(page_list)
        for y in page_list[:7]:
            if y < 0:
                # 移动到最底部
                app.down_page_use_sapce()
                if app.find_img_move_mouse_rel_click_once("./img/pagepass.png",0,y):
                    app.scroll_up_down()
                    app.close_page()
            else:
                # 移动到最顶部
                if scroll_page_find_img(300,"./img/toutiaonews.png"):
                    if app.find_img_move_mouse_rel_click_once("./img/toutiaonews.png", 0, y):
                        app.scroll_up_down()
                        app.close_page()

        # 观看视频
        app.close_page()
        app.find_img_left_mouse_click("./img/studyTV.png")
        app.down_page_use_sapce()
        app.find_img_left_mouse_click("./img/pianku.png")
        app.down_page_use_sapce()
        rand_num = random.randint(1, 15)
        # 切换页面
        for i in range(rand_num):
           app.find_img_left_mouse_click("./img/pagepass.png")
        for x in [0,-400,-800]:
            for y in [-75,-400]:
                app.find_img_move_mouse_rel_click_once("./img/pagepass.png",x,y)
                app.scroll_up_down()
                time.sleep(40)
                app.close_page()

if __name__ == '__main__':
    main()