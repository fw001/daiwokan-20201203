import page

from base.base import Base
from tool.get_log import GetLog
from asyncio import sleep

log = GetLog.get_log()


class PageLogin(Base):
    # def page_close_alert(self):
    #     self.base_click(page.login_close_alert)

    def page_swipe(self):
        # swipe 滑动
        count = 1
        while count <= 3:
            self.driver.swipe(1000, 1061, 100, 1061, duration=3000)
            sleep(1)
            count += 1  # 循环结束

    # 点击 同意并登陆
    def page_login_agree(self):
        self.base_click(page.login_agree)

    #  点击 立即体验
    def page_login_now(self):
        self.base_click(page.login_now)

    # 点击 	仅在使用中允许(定位)
    def page_login_location(self):
        self.base_click(page.login_location)

    # 点击 “我” 主页
    def page_login_me(self):
        self.base_click(page.login_me)

    # 点击 立即登录
    def page_login_log_now(self):
        self.base_click(page.login_log_now)

    # 输入用户名
    def page_input_phone(self, phone):
        # 调用 输入方法
        self.base_input(page.login_phone, phone)

    # 输入密码
    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.login_btn)

    #  返回 昵称
    def page_get_nickname(self):
        return self.base_get_text(page.login_nickname)

    # 获取 toast消息 ->登录失败
    def page_get_toast(self, msg):
        return self.base_get_toast(msg)

    # 点击 配置
    def page_click_login_setting(self):
        self.base_click(page.login_setting)

    # 点击 点击退出登录
    def page_click_log_out(self):
        self.base_click(page.login_log_out)

    # 点击 点击确认
    def page_login_confirm(self):
        self.base_click(page.login_confirm)

    # 退出登陆业务方法
    def page_logout(self):
        log.info("正在执行退出登录业务方法")
        self.page_click_login_setting()
        self.page_click_log_out()
        self.page_login_confirm()

    # 组合业务方法
    def page_login(self, phone, pwd):
        log.info("【登录业务】正在执行登录操作，用户名：{} 密码：{}".format(phone, pwd))
        # self.page_click_login_btn()
        self.page_input_phone(phone)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
