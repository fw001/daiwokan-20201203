import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tool.get_log import GetLog

# 获取日志器
log = GetLog.get_log()


class Base:
    # 初始化dirver
    @allure.step(title="初始化driver操作")
    def __init__(self, driver):
        self.driver = driver
        log.info("获取driver对象：{}".format(driver))

    # 查找元素方法
    @allure.step(title="查找元素操作")
    def base_find(self, loc, timeout=10, poll=0.5):
        # attach描述原因，不能直接为 元组
        allure.attach("查找的元素：", "{}".format(loc))
        log.info("正在查找元素：{} 超时时间：{} 访问频率：{}".format(loc, timeout, poll))
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击
    @allure.step(title="查找元素操作")
    def base_click(self, loc):
        allure.attach("点击元素：", "{}".format(loc))
        self.base_find(loc).click()
        log.info("正在点击元素：{}".format(loc))

    # 输入
    def base_input(self, loc, value):
        # 获取元素
        el = self.base_find(loc)
        # 清空
        el.clear()
        log.info("正在对元素：{} 执行清空操作".format(loc))
        # 输入
        el.send_keys(value)
        log.info("对元素：{} 执行 输入：{}".format(loc, value))

    # 获取元素文本
    def base_get_text(self, loc):
        log.info("获取：{} 元素的文本：{}".format(loc, self.base_find(loc).text))
        return self.base_find(loc).text

    # 获取toast消息
    def base_get_toast(self, msg):
        loc = By.XPATH, "//*[contains(@text,'{}')]".format(msg)
        log.info("获取包含 {}文本的 toast消息内容:{} ".format(msg, self.base_find(loc).text))
        return self.base_find(loc).text

    # 拖拽方法
    def base_drag_and_drop(self, loc1, loc2):
        el1 = self.base_find(loc1)
        el2 = self.base_find(loc2)
        # el1、el2 为两个元素
        self.driver.drag_and_drop(el1, el2)

    # 截图
    def base_get_img(self):
        # 注意：图片名写死！
        self.driver.get_screenshot_as_file("./image/err.png")
        # 将保存的图片写入 allure 报告
        self.base_write_img()

    # 将图片写入报告
    def base_write_img(self):
        with open("./image/err.png", "rb") as f:
            allure.attach("失败原因：", f.read(), allure.attach_type.PNG)
