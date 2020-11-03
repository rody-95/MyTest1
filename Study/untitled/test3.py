from selenium import webdriver#导入驱动
from time import sleep#导入休眠
dr = webdriver.Chrome()#实例化浏览器
dr.get("https://www.so.com/?src=so.com")#打开网址
dr.maximize_window()#最大化浏览器
#sleep(2)

#隐式等待
dr.implicitly_wait(10)

#定位Input输入框
Inputs = dr.find_element_by_xpath('//*[@id="input"]')
Inputs.send_keys("你是傻子")#输入内容
#定位到京公网安备
JGWAB = dr.find_element_by_xpath('//*[@id="footer"]/p/a[2]')
#获取该元素的文本，然后打印显示出来
print(JGWAB.text)
#定位搜索按钮
SearchButton = dr.find_element_by_xpath('//*[@id="search-button"]')
#获取搜索按钮的ID输入，然后打印出来
print(SearchButton.get_attribute("id"))
#查看搜索按钮是否显示,然后把 结果打印出来
print(SearchButton.is_displayed())

#实现搜索效果
SearchButton.submit()