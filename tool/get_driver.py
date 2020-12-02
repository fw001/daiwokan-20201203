from appium import webdriver


class GetDriver:
    driver = None

    # 获取driver对象
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 准备启动参数
            caps = {}
            # 设备信息
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '10'
            caps['deviceName'] = '10826625'
            # 夜神模拟器设备信息
            # caps['platformName'] = 'Android'
            # caps['platformVersion'] = '5.1'
            # caps['deviceName'] = '127.0.0.1:62001'
            # app信息
            caps['appPackage'] = 'com.qjy.teleeye'
            caps['appActivity'] = '.WelcomeActivity'
            cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            # 重点：重点：不能缩进，必须和if判断持平
        return cls.driver

    # 关闭driver对象
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            # 坑 必须置空操作
            cls.driver = None


if __name__ == '__main__':
    print("第一次获取driver对象：", GetDriver.get_driver())
    GetDriver.quit_driver()
    print("第二次获取driver对象：", GetDriver.get_driver())
