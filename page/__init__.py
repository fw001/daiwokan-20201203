from selenium.webdriver.common.by import By

"""以下为登录模块配置数据"""
# 手机号
login_phone = By.ID, "com.qjy.teleeye:id/et_reginster_phone_number"

# 密码
login_pwd = By.ID, "com.qjy.teleeye:id/et_reginster_phone_code"

# 登录按钮
login_btn = By.ID, "com.qjy.teleeye:id/tv_register_enter"

# 点击 同意并登陆
login_agree = By.ID, "com.qjy.teleeye:id/tv_home_dialog_ok"

#  点击 立即体验
login_now = By.ID, "com.qjy.teleeye:id/tv_go_app"

# 点击 	仅在使用中允许(定位)
login_location = By.CLASS_NAME, "android.widget.Button"

# 点击 “我” 主页
login_me = By.ID, "com.qjy.teleeye:id/iv_tabbar_me"

# 点击 立即登录
login_log_now = By.ID, "com.qjy.teleeye:id/tv_info_head_name"

#  昵称
login_nickname = By.ID, "com.qjy.teleeye:id/tv_info_head_name"

# 点击 配置
login_setting = By.ID, "com.qjy.teleeye:id/tv_me_setting"

# 点击 点击退出登录
login_log_out = By.ID, "com.qjy.teleeye:id/rl_config_log_out"

# 点击 点击确认
login_confirm = By.ID, "com.qjy.teleeye:id/btn_pos"
