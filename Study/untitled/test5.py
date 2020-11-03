from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("http://mail.163.com/")
dr.maximize_window()
dr.implicitly_wait(10)#隐式等待
sleep(3)
#定位Iframe,通过上层元素定位到
Frame = dr.find_element_by_xpath('//*[@id="loginDiv"]/iframe')
#切换表单
dr.switch_to.frame(Frame)

#定位账号输入框
#UserName = dr.find_element_by_xpath('//*[@id="auto-id-1556095195530"]')
UserName = dr.find_element_by_name('email')
UserName.send_keys("我爱你")

