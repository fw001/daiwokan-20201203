from page.page_login import PageLogin
from tool.get_driver import GetDriver


class PageIn:
    def __init__(self):
        self.driver = GetDriver.get_driver()

    # 获取PageLoin对象
    def page_get_pagelogin(self):
        return PageLogin(self.driver)

