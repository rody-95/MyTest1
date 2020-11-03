from selenium import webdriver#导入驱动
from time import sleep#导入休眠
from selenium.webdriver.common.action_chains import ActionChains#导入鼠标操作
dr = webdriver.Chrome()#实例化浏览器
dr.get("https://www.baidu.com/")
dr.maximize_window()#窗口最大化
dr.implicitly_wait(10)#隐式等待10s
sleep(2)
#定位设置按钮
Setting = dr.find_element_by_xpath('//*[@id="u1"]/a[8]')
#执行悬停操作
ActionChains(dr).move_to_element(Setting).perform()
sleep(2)
#定位搜索按钮
dr.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()
sleep(1)
#定位保存设置按钮
dr.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()
sleep(1)
#获取警告框内容
AlertText = dr.switch_to.alert.text
print(AlertText)
#点击警告框的确定按钮
dr.switch_to.alert.accept()
